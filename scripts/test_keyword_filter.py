"""require_keywordsフィルタのテスト（PIVOT等の非AI動画除外用）"""
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from youtube_monitor import filter_by_keywords


class TestFilterByKeywords(unittest.TestCase):
    def test_ai_video_passes(self):
        """AI関連タイトルは通過する"""
        videos = [{'video_id': 'v1', 'title': '【速報解説】アンソロピック研究者の警告/AI自律改善のリスク'}]
        result = filter_by_keywords(videos, ['AI', 'GPT', 'Claude', 'Gemini'])
        self.assertEqual(len(result), 1)

    def test_non_ai_video_filtered(self):
        """非AIタイトルは除外される"""
        videos = [
            {'video_id': 'v1', 'title': '【名車復活】パジェロ開発物語'},
            {'video_id': 'v2', 'title': 'ポルシェ911の中古市場分析'},
            {'video_id': 'v3', 'title': 'すい臓がんの初期サイン'},
        ]
        result = filter_by_keywords(videos, ['AI', 'GPT', 'Claude', 'Gemini'])
        self.assertEqual(result, [])

    def test_gemini_katakana_passes(self):
        """ジェミニ等のカタカナ表記も通過"""
        videos = [{'video_id': 'v1', 'title': 'ジェミニ仕事時短術'}]
        result = filter_by_keywords(videos, ['AI', 'Gemini', 'ジェミニ'])
        self.assertEqual(len(result), 1)

    def test_no_keywords_config_passes_all(self):
        """require_keywords未指定(None)は全通過（他チャンネルへの影響なし）"""
        videos = [{'video_id': 'v1', 'title': 'ポルシェ911'}]
        result = filter_by_keywords(videos, None)
        self.assertEqual(len(result), 1)

    def test_empty_keywords_list_passes_all(self):
        """空リストも全通過"""
        videos = [{'video_id': 'v1', 'title': 'なんでも'}]
        result = filter_by_keywords(videos, [])
        self.assertEqual(len(result), 1)

    def test_mixed(self):
        """混在ケース: AI関連のみ残る"""
        videos = [
            {'video_id': 'v1', 'title': 'ChatGPT新機能解説'},
            {'video_id': 'v2', 'title': 'バスケW杯日本代表分析'},
            {'video_id': 'v3', 'title': '生成AIで議事録作成'},
        ]
        result = filter_by_keywords(videos, ['AI', 'ChatGPT'])
        self.assertEqual([v['video_id'] for v in result], ['v1', 'v3'])


if __name__ == '__main__':
    unittest.main()
