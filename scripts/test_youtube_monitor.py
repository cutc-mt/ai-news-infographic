"""
YouTube チャンネル監視システムのテスト（TDD）
Phase 5c
"""
import pytest
import json
from unittest.mock import patch, MagicMock
import sys
import os

# scripts ディレクトリをパスに追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from youtube_monitor import (
    load_channels,
    get_channel_id,
    get_latest_videos,
    filter_new_videos,
    YouTubeMonitor,
)


class TestLoadChannels:
    """channels.yamlの読み込みテスト"""

    def test_load_channels_returns_list(self):
        channels = load_channels()
        assert isinstance(channels, list)
        assert len(channels) > 0

    def test_load_channels_has_required_fields(self):
        channels = load_channels()
        for ch in channels:
            assert 'handle' in ch
            assert 'name' in ch
            assert 'enabled' in ch

    def test_load_channels_only_enabled(self):
        channels = load_channels(only_enabled=True)
        for ch in channels:
            assert ch['enabled'] is True


class TestGetChannelId:
    """handle→channel_id変換のテスト"""

    @patch('youtube_monitor.load_channel_id_cache', return_value={})
    @patch('youtube_monitor.get_channel_id_scrape')
    @patch('youtube_monitor.requests_get')
    def test_get_channel_id_by_handle(self, mock_get, mock_scrape, mock_cache):
        mock_scrape.return_value = None  # スクレイピング失敗→APIフォールバック
        mock_get.return_value = MagicMock(
            status_code=200,
            json=MagicMock(return_value={
                'items': [{'id': 'UC123', 'snippet': {'title': 'Test'}}]
            })
        )
        with patch('youtube_monitor.save_channel_id_cache'):
            result = get_channel_id('@TestChannel', 'fake_key')
        assert result == 'UC123'

    @patch('youtube_monitor.load_channel_id_cache', return_value={})
    @patch('youtube_monitor.get_channel_id_scrape')
    @patch('youtube_monitor.requests_get')
    def test_get_channel_id_not_found(self, mock_get, mock_scrape, mock_cache):
        mock_scrape.return_value = None  # スクレイピング失敗→APIフォールバック
        mock_get.return_value = MagicMock(
            status_code=200,
            json=MagicMock(return_value={'items': []})
        )
        with patch('youtube_monitor.save_channel_id_cache'):
            result = get_channel_id('@NotFound', 'fake_key')
        assert result is None


class TestGetLatestVideos:
    """チャンネルの最新動画取得テスト"""

    @patch('youtube_monitor.requests_get')
    def test_get_latest_videos_returns_list(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=MagicMock(return_value={
                'items': [
                    {
                        'snippet': {
                            'resourceId': {'videoId': 'vid1'},
                            'title': 'Test Video 1',
                            'publishedAt': '2026-08-04T10:00:00Z',
                            'channelTitle': 'Test Channel',
                            'description': 'Test description',
                        }
                    }
                ]
            })
        )
        videos = get_latest_videos('UC123', 'fake_key', max_results=5)
        assert len(videos) == 1
        assert videos[0]['video_id'] == 'vid1'
        assert videos[0]['title'] == 'Test Video 1'

    @patch('youtube_monitor.requests_get')
    def test_get_latest_videos_empty(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=MagicMock(return_value={'items': []})
        )
        videos = get_latest_videos('UC123', 'fake_key')
        assert videos == []


class TestFilterNewVideos:
    """既存動画との重複フィルタテスト"""

    def test_filter_new_videos_excludes_known_ids(self):
        all_videos = [
            {'video_id': 'vid1', 'title': 'Old'},
            {'video_id': 'vid2', 'title': 'New'},
            {'video_id': 'vid3', 'title': 'New2'},
        ]
        known_ids = {'vid1'}
        result = filter_new_videos(all_videos, known_ids)
        assert len(result) == 2
        assert result[0]['video_id'] == 'vid2'
        assert result[1]['video_id'] == 'vid3'

    def test_filter_new_videos_all_new(self):
        all_videos = [
            {'video_id': 'vid1', 'title': 'New'},
        ]
        known_ids = set()
        result = filter_new_videos(all_videos, known_ids)
        assert len(result) == 1

    def test_filter_new_videos_all_known(self):
        all_videos = [
            {'video_id': 'vid1', 'title': 'Old'},
        ]
        known_ids = {'vid1'}
        result = filter_new_videos(all_videos, known_ids)
        assert len(result) == 0


class TestYouTubeMonitor:
    """統合監視テスト"""

    def test_monitor_returns_new_videos(self):
        monitor = YouTubeMonitor(api_key='fake_key')

        # channels.yamlを読み込む
        with patch.object(monitor, 'channels', [
            {'handle': '@TestCh', 'name': 'Test Channel', 'enabled': True}
        ]):
            with patch.object(monitor, 'get_channel_id', return_value='UC123'):
                with patch.object(monitor, 'get_latest_videos', return_value=[
                    {'video_id': 'vid1', 'title': 'New Video', 'publishedAt': '2026-08-04T10:00:00Z'}
                ]):
                    with patch.object(monitor, 'get_known_video_ids', return_value=set()):
                        # publishedAtが未来日だと日付フィルタで落ちるので、現在時刻に固定
                        with patch('youtube_monitor.datetime') as mock_dt:
                            from datetime import datetime as real_dt, timezone as real_tz
                            mock_dt.now = lambda tz=None: real_dt(2026, 8, 5, 12, 0, 0, tzinfo=real_tz.utc)
                            mock_dt.fromisoformat = real_dt.fromisoformat
                            result = monitor.check_all_channels()
                            assert len(result) == 1
                            assert result[0]['video_id'] == 'vid1'
