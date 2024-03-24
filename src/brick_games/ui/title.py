import pyray as pr  # type: ignore

from .game_menu import GameMenu


class TitleScreen:
    def __init__(self, window_width: int, window_height: int, main_font_size: int = 72) -> None:
        self.window_width = window_width
        self.window_height = window_height
        self.main_font_size = main_font_size
        self.options_font_size = self.main_font_size * 3 // 8

    def x_center_string(self, text: str, font_size: int) -> int:
        """Get the width coordinate for text."""
        text_width = pr.measure_text(text, font_size)
        x_c = (self.window_width - text_width) // 2
        return int(x_c)

    def create_title_screen(self) -> None:
        # Get x coordinates for title and quit text
        title_xc = self.x_center_string("Brick Games", self.main_font_size)

        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        # Print options to the screen
        pr.draw_text("Brick Games", title_xc, self.window_width // 4, self.main_font_size, pr.WHITE)
        menu_list = ['C to Continue', 'Q to Quit']
        game_menu = GameMenu(menu_list, 32, tr_yc=300, center_x=True)
        game_menu.draw_menu()

        if pr.is_key_pressed(pr.KeyboardKey.KEY_C):
            print("Pressing C")
            pr.clear_background(pr.WHITE)
            pr.draw_text("You are continuing", 100, 100, 72, pr.BLACK)
        if pr.is_key_pressed(pr.KeyboardKey.KEY_Q):
            print("Q has been pressed")
            pr.end_drawing()
            pr.close_window()

        pr.end_drawing()
