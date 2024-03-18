import pyray as pr  # type: ignore
from ui.title import TitleScreen  # type: ignore

""" Import Games
from games import * --> Need to check if this works
from games.<file_name> import <game Class>
from games.<file_name> import <game Class>
from games.<file_name> import <game Class>
from games.<file_name> import <game Class>
from games.<file_name> import <game Class>
from games.<file_name> import <game Class>
from games.<file_name> import <game Class>
    End of Games """

if __name__ == "__main__":
    """Begin the Title Screen"""
    title = TitleScreen(1920, 1080)  # (1280, 720), (720, 480), (640, 480)
    title.title_screen()

    # TODO: Create the Main Menu Screen
    # Move to Main Menu
    # Select Game
    # Play Game

    # TODO: Create and test the Pong class
