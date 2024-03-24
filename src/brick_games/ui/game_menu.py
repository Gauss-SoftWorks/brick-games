import pyray as pr
from .menu_item import MenuItem


class GameMenu:
    def __init__(
        self,
        menu_list: list,
        tr_xc: int = 0,
        tr_yc: int = 0,
        font_size: int = 32,
        window_width: int = 720,
        center_x: bool = False,
    ) -> None:
        self.tr_xc = tr_xc
        self.tr_yc = tr_yc
        self.menu_list = menu_list
        self.font_size = font_size
        self.window_width = window_width
        self.center_x = center_x

    def get_text_width(self, text) -> int:
        text_width = pr.measure_text(text, self.font_size)
        return int(text_width)

    def center_menu(self) -> None:
        """Automatically horizontally center text"""
        # Find longest string and find x-coordinate for center
        long_menu_item = max(self.menu_list, key=len)
        max_width_menu_item = self.get_text_width(long_menu_item)
        self.tr_xc = (self.window_width - max_width_menu_item) // 2

    def draw_menu(self) -> None:
        if self.center_x == True:
            self.center_menu()

        for index, item in enumerate(self.menu_list):
            item_xc = self.tr_xc
            item_yc = self.tr_yc + self.font_size * index
            menu_item = MenuItem(item, item_xc, item_yc, self.font_size)
            menu_item.draw_menu_item()
