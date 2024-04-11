import pyray as pr
from ui import Window
from ui import TitleScreen  # type: ignore


class GameManager:
    def __init__(self, window: Window, game_state: str = 'start') -> None:
        self.game_state = game_state

    def game_loop(self):
        # Game loop
        # Title screen -> Game Menu -> Game -> Game Menu

        while not pr.window_should_close():
            title_screen = TitleScreen(bg_color=pr.BLACK)
            self.game_state = title_screen.create_title_screen()
            if self.game_state == 'quit':
                pr.close_window()
        pr.close_window()
