import os
import unittest
from pathlib import Path
from random import random

from bangumi.parser import Parser
from bangumi.util.files import move_file, setup_test_env


class TestRawParser(unittest.TestCase):

    def setUp(self) -> None:
        self.cache_path = setup_test_env()
        return super().setUp()

    def test_output_path(self):
        parser = Parser()
        title = "【喵萌奶茶屋】★04月新番★[夏日重现/Summer Time Rendering][11][1080p][繁日双语][招募翻译] [539.4 MB]"
        episode = parser.analyse(title)
        self.assertEqual(str(episode.get_full_path(".mp4")), ".cache/media/Summer Time Rendering/Season 1/Summer Time Rendering S01E11.mp4")

        title = "【喵萌奶茶屋】★04月新番★[夏日重现/Summer Time Rendering][12][1080p][繁日双语][招募翻译] [539.4 MB]"
        episode = parser.analyse(title)
        self.assertEqual(str(episode.get_full_path(".mp4")), ".cache/media/Summer Time Rendering/Season 1/Summer Time Rendering S01E12.mp4")

        title = "【幻樱字幕组】【4月新番】【古见同学有交流障碍症 第二季 Komi-san wa, Komyushou Desu. S02】【22】【GB_MP4】【1920X1080】"
        episode = parser.analyse(title)
        self.assertEqual(str(episode.get_full_path(".mp4")), ".cache/media/Komi-san wa, Komyushou Desu./Season 2/Komi-san wa, Komyushou Desu. S02E22.mp4")


        title = "【幻樱字幕组】【4月新番】【古见同学有交流障碍症 第十季 Komi-san wa, Komyushou Desu. S10】【201】【GB_MP4】【1920X1080】"
        episode = parser.analyse(title)
        self.assertEqual(str(episode.get_full_path(".mp4")), ".cache/media/Komi-san wa, Komyushou Desu./Season 10/Komi-san wa, Komyushou Desu. S10E201.mp4")

    def test_move_file(self):
        parser = Parser()
        title = "【幻樱字幕组】【4月新番】【古见同学有交流障碍症 第十季 Komi-san wa, Komyushou Desu. S10】【201】【GB_MP4】【1920X1080】"
        episode = parser.analyse(title)

        val = str(random())
        filename = Path("test")
        with open(self.cache_path / filename, "w") as f:
            f.write(val)
        move_file(filename, episode)
        self.assertTrue(os.path.exists(episode.get_full_path("")))
        with open(episode.get_full_path(""), "r") as f:
            self.assertEqual(f.read(), val)
