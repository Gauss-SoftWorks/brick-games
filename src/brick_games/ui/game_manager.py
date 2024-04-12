import pyray as pr
from ui import Window
from ui import GameSelect
from ui import TitleScreen  # type: ignore


class GameManager:
    def __init__(self, window: Window, game_state: str = 'start') -> None:
        self.game_state = game_state
        self.title_screen = None

    def game_loop(self):
        # Game loop
        # Title screen -> Game Menu -> Game -> Game Menu
        while not pr.window_should_close():
            match self.game_state:
                case 'start':
                    print('Starting game')
                    self.game_state = 'title_screen'
                case 'title_screen':
                    print('entering title screen')
                    # Title screen logic
                    if pr.is_key_pressed(pr.KeyboardKey.KEY_C):
                        print("Pressing C")
                        self.game_state = 'game_select'
                    elif pr.is_key_pressed(pr.KeyboardKey.KEY_Q):
                        print("Q has been pressed")
                        self.game_state = 'quit'
                case 'game_select':
                    print('entering game select.')
                    if pr.is_key_pressed(pr.KeyboardKey.KEY_B):
                        print("Pressing B")
                        self.game_state = 'title_screen'
                    elif pr.is_key_pressed(pr.KeyboardKey.KEY_Q):
                        print("Q has been pressed")
                        self.game_state = 'quit'
                case 'quit':
                    pr.close_window()
            # Second Loop
            match self.game_state:
                case 'title_screen':
                    print('entering 2nd loop.')
                    self.title_screen = TitleScreen(bg_color=pr.BLACK)
                    self.title_screen.create_title_screen()
                case 'game_select':
                    self.game_select = GameSelect(game_list=['Hello', 'World'])
                    self.game_select.create_game_select()

        pr.close_window()
