"""
API更新スクリプトのテスト（TDD）
Phase 5e: インフォグラフィック生成後のAPI更新
"""
import pytest
import json
from unittest.mock import patch, MagicMock
import sys
import os
from urllib.error import HTTPError

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from update_news import (
    build_infographic_url,
    update_news_entry,
    update_batch,
)


class TestBuildInfographicUrl:
    """ファイル名からGitHub Pages URLを構築"""

    def test_basic_url(self):
        url = build_infographic_url('20260804-GPT6-解説-WorldofAI.html')
        assert 'github.io' in url
        assert '20260804-GPT6' in url
        assert url.endswith('.html')

    def test_url_contains_docs_path(self):
        url = build_infographic_url('test.html')
        assert '/docs/' in url


class TestUpdateNewsEntry:
    """API PUT のテスト"""

    @patch('update_news.urllib.request.urlopen')
    def test_update_success(self, mock_urlopen):
        mock_resp = MagicMock()
        mock_resp.status = 200
        mock_resp.read.return_value = b'{"id": 1}'
        mock_urlopen.return_value.__enter__.return_value = mock_resp

        result = update_news_entry(
            news_id=1,
            api_url='http://localhost:8000/api/news/1',
            title='日本語タイトル',
            summary='日本語概要',
            infographic_url='https://example.com/test.html',
        )
        assert result is True

    @patch('update_news.urllib.request.urlopen')
    def test_update_not_found(self, mock_urlopen):
        mock_urlopen.side_effect = HTTPError(
            'url', 404, 'Not Found', {}, b''
        )
        result = update_news_entry(
            news_id=999,
            api_url='http://localhost:8000/api/news/999',
            title='テスト',
            summary='テスト',
            infographic_url='',
        )
        assert result is False

    def test_update_only_infographic_url(self):
        """infographic_urlのみ更新"""
        with patch('update_news.urllib.request.urlopen') as mock_urlopen:
            mock_resp = MagicMock()
            mock_resp.status = 200
            mock_resp.read.return_value = b'{"id": 1}'
            mock_urlopen.return_value.__enter__.return_value = mock_resp

            result = update_news_entry(
                news_id=1,
                api_url='http://localhost:8000/api/news/1',
                infographic_url='https://example.com/test.html',
            )
            assert result is True


class TestUpdateBatch:
    """バッチ更新のテスト"""

    @patch('update_news.update_news_entry')
    def test_batch_all_success(self, mock_update):
        mock_update.return_value = True
        entries = [
            {'news_id': 1, 'title': 'タイトル1', 'summary': '概要1',
             'infographic_url': 'https://example.com/1.html'},
            {'news_id': 2, 'title': 'タイトル2', 'summary': '概要2',
             'infographic_url': 'https://example.com/2.html'},
        ]
        results = update_batch(entries, api_base='http://localhost:8000')
        assert results['success'] == 2
        assert results['failed'] == 0

    @patch('update_news.update_news_entry')
    def test_batch_mixed(self, mock_update):
        mock_update.side_effect = [True, False]
        entries = [
            {'news_id': 1, 'title': 'タイトル1', 'summary': '概要1',
             'infographic_url': 'https://example.com/1.html'},
            {'news_id': 2, 'title': 'タイトル2', 'summary': '概要2',
             'infographic_url': 'https://example.com/2.html'},
        ]
        results = update_batch(entries, api_base='http://localhost:8000')
        assert results['success'] == 1
        assert results['failed'] == 1
