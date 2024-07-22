import pyray as pr  # type: ignore


class MenuItem:
    def __init__(
        self, text: str, xc: int = 0, yc: int = 0, font_size: int = 32, text_color: pr.Color = pr.WHITE
    ) -> None:
        self.text = text
        self.xc = xc
        self.yc = yc
        self.font_size = font_size
        self.text_color = text_color

    def draw_menu_item(self) -> None:
        pr.draw_text(self.text, self.xc, self.yc, self.font_size, self.text_color)
