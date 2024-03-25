import unittest

import pyray as pr  # type: ignore:

from brick_games.ui.title_screen import TitleScreen


class TestTitleScreen(unittest.TestCase):
    def tearUp(self, bg_color: pr.Color = pr.WHITE) -> None:
        self.bg_color = bg_color
        self.title = TitleScreen(self.bg_color)
        pass

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self) -> None:
        self.tearUp()
        self.assertEqual(pr.WHITE, self.title.bg_color)

        self.tearDown()
        self.tearUp(pr.BLACK)
        self.assertEqual(pr.BLACK, self.title.bg_color)
