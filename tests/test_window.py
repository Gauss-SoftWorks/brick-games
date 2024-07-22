import unittest

import pyray as pr  # type: ignore:

from brick_games.ui.window import Window


class TestWindow(unittest.TestCase):
    def tearUp(self, width: int, height: int, title: str) -> None:
        self.window = Window(width, height, title)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self) -> None:
        self.tearUp(1920, 1080, "Testing Title")
        self.assertEqual(self.window.width, 1920)
        self.assertEqual(self.window.height, 1080)
        self.assertEqual(self.window.window_title, "Testing Title")
        self.tearDown()
