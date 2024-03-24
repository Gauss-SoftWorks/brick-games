import pyray as pr  # type: ignore

from ui import TitleScreen  # type: ignore
from ui import Window


# from games import *

if __name__ == "__main__":
    """Begin the Title Screen"""
    window_width = 720
    window_height = 480
    game_title = "Brick Games"

    window = Window(window_width, window_height, game_title)
    window.create_window()

    while not pr.window_should_close():
        # main game loop
        title_screen = TitleScreen(bg_color=pr.BLACK)
        title_screen.create_title_screen()

    pr.close_window()

    # TODO: Create the Main Menu Screen
    # Move to Main Menu
    # Select Game
    # Play Game

    # TODO: Create and test the Pong class
