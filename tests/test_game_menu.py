import unittest

import pyray as pr  # type: ignore:

from brick_games.ui.game_menu import GameMenu


class TestGameTitle(unittest.TestCase):
    def tearUp(
        self,
        menu_list: list[str],
        tr_xc: int = 0,
        tr_yc: int = 0,
        font_size: int = 32,
        window_width: int = 720,
        center_x: bool = False,
    ) -> None:
        self.game_title = GameMenu(menu_list, tr_xc, tr_yc, font_size, window_width, center_x)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self) -> None:
        self.tearUp(["One", "Two"], 1, 2, 100, 1080, True)
        self.assertEqual(self.game_title.menu_list, ["One", "Two"])
        self.assertEqual(self.game_title.tr_xc, 1)
        self.assertEqual(self.game_title.tr_yc, 2)
        self.assertEqual(self.game_title.font_size, 100)
        self.assertEqual(self.game_title.window_width, 1080)
        self.assertEqual(self.game_title.center_x, True)
        self.tearDown()

        self.tearUp(["One", "Two"])
        self.assertEqual(self.game_title.menu_list, ["One", "Two"])
        self.assertEqual(self.game_title.tr_xc, 0)
        self.assertEqual(self.game_title.tr_yc, 0)
        self.assertEqual(self.game_title.font_size, 32)
        self.assertEqual(self.game_title.window_width, 720)
        self.assertEqual(self.game_title.center_x, False)
        self.tearDown()
