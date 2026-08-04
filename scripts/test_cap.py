"""
新着動画上限のテスト（TDD）
1回の監視で最大30件までに制限
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from post_news import cap_videos


class TestCapVideos:
    """新着動画の上限テスト"""

    def test_under_limit(self):
        videos = [{'video_id': f'v{i}', 'title': f'T{i}'} for i in range(10)]
        result = cap_videos(videos, max_count=30)
        assert len(result) == 10

    def test_at_limit(self):
        videos = [{'video_id': f'v{i}', 'title': f'T{i}'} for i in range(30)]
        result = cap_videos(videos, max_count=30)
        assert len(result) == 30

    def test_over_limit(self):
        videos = [{'video_id': f'v{i}', 'title': f'T{i}'} for i in range(50)]
        result = cap_videos(videos, max_count=30)
        assert len(result) == 30

    def test_empty(self):
        result = cap_videos([], max_count=30)
        assert len(result) == 0

    def test_custom_limit(self):
        videos = [{'video_id': f'v{i}', 'title': f'T{i}'} for i in range(10)]
        result = cap_videos(videos, max_count=5)
        assert len(result) == 5
