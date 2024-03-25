import pyray as pr  # type: ignore

from .game_menu import GameMenu
from .game_title import GameTitle


class TitleScreen:
    def __init__(self, bg_color: pr.Color = pr.WHITE) -> None:
        self.bg_color = bg_color

    def create_title_screen(self) -> None:
        pr.begin_drawing()
        pr.clear_background(self.bg_color)

        # GameTitle object
        # TODO: Access global game title variable
        title = GameTitle('Brick Games', yc=120, color=pr.WHITE)
        title.draw_title()

        # Menu Object
        menu_list = ['C to Continue', 'Q to Quit']
        game_menu = GameMenu(menu_list, 32, tr_yc=300, center_x=True)
        game_menu.draw_menu()

        # Title screen logic
        if pr.is_key_pressed(pr.KeyboardKey.KEY_C):
            print("Pressing C")
            pr.clear_background(pr.WHITE)
            pr.draw_text("You are continuing", 100, 100, 72, pr.BLACK)
        if pr.is_key_pressed(pr.KeyboardKey.KEY_Q):
            print("Q has been pressed")
            pr.end_drawing()
            pr.close_window()

        pr.end_drawing()
