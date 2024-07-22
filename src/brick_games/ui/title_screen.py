import pyray as pr  # type: ignore

from .game_menu import GameMenu
from .game_title import GameTitle


class TitleScreen:
    def __init__(self, bg_color: pr.Color = pr.WHITE) -> None:
        self.bg_color = bg_color

    def create_title_screen(self) -> str:
        game_state = 'title_screen'
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

        pr.end_drawing()
        return game_state
