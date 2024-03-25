import unittest

import pyray as pr  # type: ignore:

from brick_games.ui.menu_item import MenuItem


class TestMenuItem(unittest.TestCase):
    def tearUp(self, text: str, xc: int = 0, yc: int = 0, font_size: int = 32, text_color: pr.Color = pr.WHITE) -> None:
        self.menu_item = MenuItem(text, xc, yc, font_size, text_color)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self) -> None:
        self.tearUp("Main Menu")
        self.assertEqual(self.menu_item.text, "Main Menu")
        self.assertEqual(self.menu_item.xc, 0)
        self.assertEqual(self.menu_item.yc, 0)
        self.assertEqual(self.menu_item.font_size, 32)
        self.assertEqual(self.menu_item.text_color, pr.WHITE)
        self.tearDown()
        self.tearUp("Test", 1, 2, 100, pr.BLACK)
        self.assertEqual(self.menu_item.text, "Test")
        self.assertEqual(self.menu_item.xc, 1)
        self.assertEqual(self.menu_item.yc, 2)
        self.assertEqual(self.menu_item.font_size, 100)
        self.assertEqual(self.menu_item.text_color, pr.BLACK)
        self.tearDown()
