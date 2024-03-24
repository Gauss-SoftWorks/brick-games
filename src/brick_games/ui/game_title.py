import pyray as pr  # type: ignore
from .helper import center_text_x


class GameTitle:
    def __init__(
        self,
        game_title: str,
        xc: int = 0,
        yc: int = 0,
        font_size: int = 72,
        color: pr.Color = pr.BLACK,
        center_x: bool = True,
    ) -> None:
        self.game_title = game_title
        self.xc = xc
        self.yc = yc
        self.font_size = font_size
        self.color = color
        self.center_x = center_x

    def draw_title(self) -> None:
        if self.center_x == True:
            self.xc = center_text_x(self.game_title, self.font_size)

        pr.draw_text(self.game_title, self.xc, self.yc, self.font_size, self.color)
