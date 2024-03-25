import pyray as pr  # type: ignore

IMAGE_NAME = 'games-six-six-six.png'


class Window:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.window_title = title

    def create_window(self) -> None:
        """Create window"""
        # TODO: Remove hard coded window image and fps.
        window_icon = pr.load_image(IMAGE_NAME)
        pr.init_window(self.width, self.height, self.window_title)
        pr.set_target_fps(60)
        pr.set_window_icon(window_icon)
