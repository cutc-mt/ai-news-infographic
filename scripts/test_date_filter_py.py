"""
新着動画の日付フィルタのテスト（TDD）
監視時点から指定日数以内の動画のみを対象とする
"""
import pytest
import sys
import os
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from youtube_monitor import filter_by_date, is_recent


class TestIsRecent:
    """動画が指定日数以内か判定"""

    def test_video_from_today(self):
        now = datetime.now(timezone.utc)
        pub = now.isoformat()
        assert is_recent(pub, max_days=1) is True

    def test_video_from_12h_ago(self):
        now = datetime.now(timezone.utc)
        pub = (now - timedelta(hours=12)).isoformat()
        assert is_recent(pub, max_days=1) is True

    def test_video_from_3_days_ago(self):
        now = datetime.now(timezone.utc)
        pub = (now - timedelta(days=3)).isoformat()
        assert is_recent(pub, max_days=1) is False

    def test_video_from_2_days_ago_within_3day_limit(self):
        now = datetime.now(timezone.utc)
        pub = (now - timedelta(days=2)).isoformat()
        assert is_recent(pub, max_days=3) is True

    def test_video_7_days_ago_within_7day_limit(self):
        now = datetime.now(timezone.utc)
        pub = (now - timedelta(days=6, hours=23)).isoformat()
        assert is_recent(pub, max_days=7) is True

    def test_invalid_date_string(self):
        assert is_recent('invalid', max_days=1) is False

    def test_empty_date(self):
        assert is_recent('', max_days=1) is False


class TestFilterByDate:
    """動画リストを日付で絞り込む"""

    def test_filters_old_videos(self):
        now = datetime.now(timezone.utc)
        videos = [
            {'video_id': 'v1', 'publishedAt': now.isoformat()},
            {'video_id': 'v2', 'publishedAt': (now - timedelta(days=5)).isoformat()},
            {'video_id': 'v3', 'publishedAt': (now - timedelta(days=30)).isoformat()},
        ]
        result = filter_by_date(videos, max_days=1)
        assert len(result) == 1
        assert result[0]['video_id'] == 'v1'

    def test_all_recent(self):
        now = datetime.now(timezone.utc)
        videos = [
            {'video_id': 'v1', 'publishedAt': now.isoformat()},
            {'video_id': 'v2', 'publishedAt': (now - timedelta(hours=6)).isoformat()},
        ]
        result = filter_by_date(videos, max_days=1)
        assert len(result) == 2

    def test_all_old(self):
        now = datetime.now(timezone.utc)
        videos = [
            {'video_id': 'v1', 'publishedAt': (now - timedelta(days=30)).isoformat()},
        ]
        result = filter_by_date(videos, max_days=1)
        assert len(result) == 0

    def test_empty_list(self):
        result = filter_by_date([], max_days=1)
        assert result == []

    def test_3_day_window(self):
        now = datetime.now(timezone.utc)
        videos = [
            {'video_id': 'v1', 'publishedAt': (now - timedelta(days=1)).isoformat()},
            {'video_id': 'v2', 'publishedAt': (now - timedelta(days=2)).isoformat()},
            {'video_id': 'v3', 'publishedAt': (now - timedelta(days=5)).isoformat()},
        ]
        result = filter_by_date(videos, max_days=3)
        assert len(result) == 2
