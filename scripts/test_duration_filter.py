"""
動画の長さフィルタのテスト（TDD）
- 5分未満の動画はインフォグラフィック対象外
- videos.list APIでdurationを一括取得
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from youtube_monitor import parse_duration, get_video_durations, filter_by_duration


class TestParseDuration:
    """ISO 8601 durationのパース"""

    def test_minutes_and_seconds(self):
        assert parse_duration('PT4M30S') == 270

    def test_hours(self):
        assert parse_duration('PT1H2M3S') == 3723

    def test_seconds_only(self):
        assert parse_duration('PT30S') == 30

    def test_days(self):
        assert parse_duration('P1DT2H') == 93600

    def test_empty(self):
        assert parse_duration('') == 0

    def test_invalid(self):
        assert parse_duration('garbage') == 0


class TestFilterByDuration:
    """5分（300秒）未満の動画を除外"""

    def test_filters_short_videos(self):
        videos = [{'video_id': 'aaa'}, {'video_id': 'bbb'}, {'video_id': 'ccc'}]
        durations = {'aaa': 600, 'bbb': 120, 'ccc': 300}
        result = filter_by_duration(videos, durations, min_seconds=300)
        assert [v['video_id'] for v in result] == ['aaa', 'ccc']

    def test_boundary_exact_5min_is_kept(self):
        videos = [{'video_id': 'xxx'}]
        durations = {'xxx': 300}
        result = filter_by_duration(videos, durations, min_seconds=300)
        assert len(result) == 1

    def test_unknown_duration_is_kept(self):
        """API失敗等で長さ不明な動画は誤除外を防ぐため残す"""
        videos = [{'video_id': 'zzz'}]
        result = filter_by_duration(videos, {}, min_seconds=300)
        assert len(result) == 1


class TestGetVideoDurations:
    """videos.list APIの一括取得"""

    def test_batch_request_format(self, monkeypatch):
        captured_url = {}

        def mock_get(url):
            captured_url['url'] = url
            return {'status_code': 200, 'json': lambda: {
                'items': [
                    {'id': 'aaa', 'contentDetails': {'duration': 'PT10M'}},
                    {'id': 'bbb', 'contentDetails': {'duration': 'PT2M'}},
                ]
            }}

        monkeypatch.setattr('youtube_monitor.requests_get', mock_get)
        durations = get_video_durations(['aaa', 'bbb'], 'FAKE_KEY')
        assert durations == {'aaa': 600, 'bbb': 120}
        assert 'part=contentDetails' in captured_url['url']
        assert 'id=aaa,bbb' in captured_url['url']

    def test_empty_list(self):
        assert get_video_durations([], 'FAKE_KEY') == {}
