import unittest

import pyray as pr  # type: ignore:

from brick_games.ui.helper import center_text_x


class TestHelper(unittest.TestCase):
    def tearUp(self, text: str = "testing", font_size: int = 32) -> None:
        self.text = text
        self.screen_width = pr.get_screen_height()
        self.font_size = font_size

    def tearDown(self) -> None:
        return super().tearDown()

    def test_center_text_x(self) -> None:
        self.tearUp()
        x_coordinate = center_text_x("testing", 32)
        test_width = pr.measure_text(self.text, self.font_size)
        self.assertEqual(x_coordinate, test_width)
        self.tearDown()
        self.tearUp()
        x_coordinate = center_text_x("UNION", 100)
        test_width = pr.measure_text(self.text, self.font_size)
        self.assertEqual(x_coordinate, test_width)
        self.tearDown()
