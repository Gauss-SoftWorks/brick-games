import pyray as pr  # type: ignore


class Window:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.window_title = title

    def create_window(self) -> None:
        """Create window"""
        pr.init_window(self.width, self.height, self.window_title)
        pr.set_target_fps(60)
