import unittest

import pyray as pr  # type: ignore:

from brick_games.ui.game_title import GameTitle


class TestGameTitle(unittest.TestCase):
    def tearUp(
        self,
        game_title: str,
        xc: int = 0,
        yc: int = 0,
        font_size: int = 72,
        color: pr.Color = pr.BLACK,
        center_x: bool = True,
    ) -> None:
        self.game_title = GameTitle(game_title, xc, yc, font_size, color, center_x)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self) -> None:
        self.tearUp("Title")
        self.assertEqual(self.game_title.game_title, "Title")
        self.assertEqual(self.game_title.xc, 0)
        self.assertEqual(self.game_title.yc, 0)
        self.assertEqual(self.game_title.font_size, 72)
        self.assertEqual(self.game_title.color, pr.BLACK)
        self.assertEqual(self.game_title.center_x, True)
        self.tearDown()

        self.tearUp("Eva", 1, 2, 100, pr.GREEN, False)
        self.assertEqual(self.game_title.game_title, "Eva")
        self.assertEqual(self.game_title.xc, 1)
        self.assertEqual(self.game_title.yc, 2)
        self.assertEqual(self.game_title.font_size, 100)
        self.assertEqual(self.game_title.color, pr.GREEN)
        self.assertEqual(self.game_title.center_x, False)
        self.tearDown()
