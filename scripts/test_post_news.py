"""
ニュースAPI POST スクリプトのテスト（TDD）
Phase 5d
"""
import pytest
import json
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from post_news import (
    build_news_payload,
    post_news,
    batch_post_news,
)


class TestBuildNewsPayload:
    """YouTube動画情報からAPIペイロードを構築"""

    def test_build_payload_basic(self):
        video = {
            'video_id': 'abc123',
            'title': 'GPT-6リリース',
            'description': 'OpenAIの新モデル',
            'channel_title': 'World of AI',
            'channel_name': 'World of AI',
            'channel_handle': '@WorldofAI',
            'publishedAt': '2026-08-04T10:00:00Z',
            'url': 'https://www.youtube.com/watch?v=abc123',
        }
        payload = build_news_payload(video)

        assert payload['title'] == 'GPT-6リリース'
        assert payload['source'] == 'World of AI'
        assert payload['date'] == '2026-08-04'
        assert payload['url'] == 'https://www.youtube.com/watch?v=abc123'
        assert payload['video_id'] == 'abc123'
        assert payload['channel_id'] == '@WorldofAI'
        assert 'summary' in payload
        assert 'category' in payload

    def test_build_payload_summary_from_description(self):
        video = {
            'video_id': 'vid1',
            'title': 'Test',
            'description': 'This is a test description',
            'channel_name': 'TestCh',
            'channel_handle': '@test',
            'publishedAt': '2026-08-04T10:00:00Z',
            'url': 'https://www.youtube.com/watch?v=vid1',
        }
        payload = build_news_payload(video)
        assert payload['summary'] == 'This is a test description'

    def test_build_payload_empty_description(self):
        video = {
            'video_id': 'vid1',
            'title': 'Test',
            'description': '',
            'channel_name': 'TestCh',
            'channel_handle': '@test',
            'publishedAt': '2026-08-04T10:00:00Z',
            'url': 'https://www.youtube.com/watch?v=vid1',
        }
        payload = build_news_payload(video)
        assert payload['summary'] != ''  # フォールバック


class TestPostNews:
    """APIへのPOSTテスト"""

    @patch('post_news.urllib.request.urlopen')
    def test_post_news_success(self, mock_urlopen):
        mock_resp = MagicMock()
        mock_resp.status = 200
        mock_resp.read.return_value = b'{"id": 7}'
        mock_urlopen.return_value.__enter__.return_value = mock_resp

        result = post_news(
            {'title': 'Test', 'summary': 'Test', 'source': 'Test',
             'date': '2026-08-04', 'category': 'AIニュース',
             'url': 'https://example.com', 'tags': '', 'video_id': 'vid1',
             'channel_id': '@test', 'infographic_url': ''},
            api_url='http://localhost:8000/api/news'
        )
        assert result is True

    @patch('post_news.urllib.request.urlopen')
    def test_post_news_duplicate_409(self, mock_urlopen):
        """重複video_idの場合は409が返る"""
        from urllib.error import HTTPError
        mock_urlopen.side_effect = HTTPError(
            'url', 409, 'Conflict', {}, b'{"detail": "already exists"}'
        )
        result = post_news(
            {'title': 'Test', 'summary': 'Test', 'source': 'Test',
             'date': '2026-08-04', 'category': 'AIニュース',
             'url': 'https://example.com', 'tags': '', 'video_id': 'vid1',
             'channel_id': '@test', 'infographic_url': ''},
            api_url='http://localhost:8000/api/news'
        )
        # 重複は正常終了として扱う（スキップ）
        assert result is True

    @patch('post_news.urllib.request.urlopen')
    def test_post_news_server_error(self, mock_urlopen):
        from urllib.error import HTTPError
        mock_urlopen.side_effect = HTTPError(
            'url', 500, 'Server Error', {}, b'{"detail": "error"}'
        )
        result = post_news(
            {'title': 'Test', 'summary': 'Test', 'source': 'Test',
             'date': '2026-08-04', 'category': 'AIニュース',
             'url': 'https://example.com', 'tags': '', 'video_id': 'vid1',
             'channel_id': '@test', 'infographic_url': ''},
            api_url='http://localhost:8000/api/news'
        )
        assert result is False


class TestBatchPostNews:
    """バッチPOSTのテスト"""

    @patch('post_news.post_news')
    def test_batch_post_all_success(self, mock_post):
        mock_post.return_value = True
        videos = [
            {'video_id': f'vid{i}', 'title': f'Test {i}', 'description': 'desc',
             'channel_name': 'Ch', 'channel_handle': '@ch',
             'publishedAt': '2026-08-04T10:00:00Z',
             'url': f'https://youtube.com/watch?v=vid{i}'}
            for i in range(3)
        ]
        results = batch_post_news(videos, api_url='http://localhost:8000/api/news')
        assert results['success'] == 3
        assert results['failed'] == 0
        assert results['skipped'] == 0

    @patch('post_news.post_news')
    def test_batch_post_mixed_results(self, mock_post):
        mock_post.side_effect = [True, False, True]
        videos = [
            {'video_id': f'vid{i}', 'title': f'Test {i}', 'description': 'desc',
             'channel_name': 'Ch', 'channel_handle': '@ch',
             'publishedAt': '2026-08-04T10:00:00Z',
             'url': f'https://youtube.com/watch?v=vid{i}'}
            for i in range(3)
        ]
        results = batch_post_news(videos, api_url='http://localhost:8000/api/news')
        assert results['success'] == 2
        assert results['failed'] == 1
