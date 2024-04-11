import pyray as pr  # type: ignore
from ui import Window
from ui import GameManager

# from games import *

if __name__ == "__main__":
    """Begin the Title Screen"""
    window_width = 720
    window_height = 480
    game_title = "Brick Games"

    window = Window(window_width, window_height, game_title)
    window.create_window()

    game_manager = GameManager(window, game_state='start')
    game_manager.game_loop()
