"""未解決チャンネル（handle変更・削除済み）の検知テスト"""
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from youtube_monitor import YouTubeMonitor, load_channels


class TestUnresolvedChannelReporting(unittest.TestCase):
    """check_all_channelsが未解決チャンネルを報告するかのテスト"""

    def setUp(self):
        # channels.yamlの代わりにインメモリのチャンネルリストを使う
        self.channels = [
            {'handle': '@dead_channel', 'name': '消えたチャンネル', 'enabled': True},
            {'handle': '@alive_channel', 'name': '生きてるチャンネル', 'enabled': True},
        ]

    @patch('youtube_monitor.load_channels')
    def test_unresolved_channel_reported(self, mock_load):
        """handleが解決できないチャンネルは unresolved リストに入る"""
        mock_load.return_value = self.channels

        monitor = YouTubeMonitor(api_key='fake_key')

        # get_channel_idをモック: dead_channel→None, alive_channel→ID
        def mock_get_channel_id(handle):
            return 'UC_alive_123' if handle == '@alive_channel' else None

        with patch.object(monitor, 'get_channel_id', side_effect=mock_get_channel_id):
            with patch.object(monitor, 'get_latest_videos', return_value=[]):
                with patch.object(monitor, 'get_known_video_ids', return_value=set()):
                    result = monitor.check_all_channels()

        # 戻り値の構造: {'videos': [], 'unresolved': [{'handle', 'name'}]}
        self.assertIsInstance(result, dict)
        self.assertEqual(result['videos'], [])
        self.assertEqual(len(result['unresolved']), 1)
        self.assertEqual(result['unresolved'][0]['handle'], '@dead_channel')
        self.assertEqual(result['unresolved'][0]['name'], '消えたチャンネル')

    @patch('youtube_monitor.load_channels')
    def test_all_resolved_no_unresolved(self, mock_load):
        """全チャンネル解決時はunresolvedは空リスト"""
        mock_load.return_value = self.channels

        monitor = YouTubeMonitor(api_key='fake_key')

        def mock_get_channel_id(handle):
            return f'UC_{handle[1:]}'  # 全部解決

        with patch.object(monitor, 'get_channel_id', side_effect=mock_get_channel_id):
            with patch.object(monitor, 'get_latest_videos', return_value=[]):
                with patch.object(monitor, 'get_known_video_ids', return_value=set()):
                    result = monitor.check_all_channels()

        self.assertEqual(result['videos'], [])
        self.assertEqual(result['unresolved'], [])


if __name__ == '__main__':
    unittest.main()
