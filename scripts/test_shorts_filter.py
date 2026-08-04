"""
ショート動画除外フィルターのテスト（TDD）
Phase 5c: Shorts（60秒以下）を監視対象から除外
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from youtube_monitor import filter_shorts, is_likely_short


class TestIsLikelyShort:
    """タイトル/説明文からショート動画か判定"""

    def test_hashtag_short(self):
        assert is_likely_short({'title': 'テスト #shorts', 'description': ''}) is True

    def test_hashtag_short_uppercase(self):
        assert is_likely_short({'title': 'Amazing AI #Shorts', 'description': ''}) is True

    def test_normal_video(self):
        assert is_likely_short({'title': 'GPT-6完全解説', 'description': '長い動画です'}) is False

    def test_description_has_shorts(self):
        assert is_likely_short({'title': 'テスト', 'description': '#shorts #ai'}) is True

    def test_title_has_short(self):
        assert is_likely_short({'title': 'AIすごい[short]', 'description': ''}) is True


class TestFilterShorts:
    """動画リストからショート動画を除外"""

    def test_removes_shorts_by_hashtag(self):
        videos = [
            {'video_id': 'v1', 'title': '普通の動画', 'description': ''},
            {'video_id': 'v2', 'title': 'ショート #shorts', 'description': ''},
            {'video_id': 'v3', 'title': '別のショート #Shorts', 'description': ''},
            {'video_id': 'v4', 'title': '解説動画', 'description': '長文'},
        ]
        result = filter_shorts(videos)
        assert len(result) == 2
        assert result[0]['video_id'] == 'v1'
        assert result[1]['video_id'] == 'v4'

    def test_all_normal_returns_all(self):
        videos = [
            {'video_id': 'v1', 'title': '動画1', 'description': ''},
            {'video_id': 'v2', 'title': '動画2', 'description': ''},
        ]
        result = filter_shorts(videos)
        assert len(result) == 2

    def test_all_shorts_returns_empty(self):
        videos = [
            {'video_id': 'v1', 'title': '#shorts', 'description': ''},
            {'video_id': 'v2', 'title': '#Shorts', 'description': ''},
        ]
        result = filter_shorts(videos)
        assert len(result) == 0

    def test_empty_list(self):
        result = filter_shorts([])
        assert result == []
