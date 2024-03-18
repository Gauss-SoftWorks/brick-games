import pyray as pr  # type: ignore

""" Import Title Screen """
from ui.title import TitleScreen  # type: ignore

""" Import Games """
# from games import * --> Need to check if this works
# from games.<file_name> import <game Class>
# from games.<file_name> import <game Class>
# from games.<file_name> import <game Class>
# from games.<file_name> import <game Class>
# from games.<file_name> import <game Class>
# from games.<file_name> import <game Class>
# from games.<file_name> import <game Class>
""" End of Games """

""" Temaplate """
# pr.init_window(800, 450, "Hello Pyray")
# pr.set_target_fps(60)
#
# camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0],
#                      [0.0, 1.0, 0.0], 45.0, 0)
#
# while not pr.window_should_close():
#     pr.update_camera(camera, pr.CAMERA_ORBITAL)
#     pr.begin_drawing()
#     pr.clear_background(pr.RAYWHITE)
#     pr.begin_mode_3d(camera)
#     pr.draw_grid(20, 1.0)
#     pr.end_mode_3d()
#     pr.draw_text("Hello world", 190, 200, 20, pr.VIOLET)
#     pr.end_drawing()
# pr.close_window()
""" End of Temaplate """

""" Main Class """


def main() -> None:
    """Begin the Title Screen"""
    title = TitleScreen(1920, 1080)  # (1280, 720), (720, 480), (640, 480)
    title.title_screen()

    # TODO: Create the Main Menu Screen
    # Move to Main Menu
    # Select Game
    # Play Game

    # TODO: Create and test the Pong class


if __name__ == "__main__":
    main()
