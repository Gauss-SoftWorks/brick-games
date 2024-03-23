import pyray as pr  # type: ignore

from ui import TitleScreen  # type: ignore
from ui import Window  # type: ignore

# from games import *

if __name__ == "__main__":
    """Begin the Title Screen"""
    window = Window(720, 480, "Brick Games")
    print(window.height)
    window.create_window()

    while not pr.window_should_close():
        # main game loop
        title_screen = TitleScreen(window.width, window.height)
        title_screen.create_title_screen()

    pr.close_window()

    # TODO: Create the Main Menu Screen
    # Move to Main Menu
    # Select Game
    # Play Game

    # TODO: Create and test the Pong class
