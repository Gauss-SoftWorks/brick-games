from brick_games.ui.title import TitleScreen
import pyray as pr
import unittest


class TestTitleScreen(unittest.TestCase):
    def tearUp(self, width: int, height: int, font: int = 72) -> None:
        self.width = width
        self.height = height
        self.font = font
        self.text = "Brick Games"
        self.title = TitleScreen(self.width, self.height, self.font)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self) -> None:
        self.tearUp(1920, 1080, 100)
        self.assertEqual(1920, self.title.width)
        self.assertEqual(1080, self.title.height)
        self.assertEqual(100, self.title.font)
        self.tearDown()
        self.tearUp(1920, 1080)
        self.assertEqual(72, self.title.font)
        self.tearDown()

    def test_get_width_position(self) -> None:
        self.tearUp(1920, 1080)
        text_width = pr.measure_text(self.text, self.font)
        x_coord = int((self.width - text_width) // 2)
        method_coord = self.title.get_width_position(self.text, self.font)
        self.assertEqual(x_coord, method_coord)
        self.tearDown()

        self.tearUp(640, 480)
        text_width = pr.measure_text(self.text, self.font)
        x_coord = int((self.width - text_width) // 2)
        method_coord = self.title.get_width_position(self.text, self.font)
        self.assertEqual(x_coord, method_coord)
        self.tearDown()
