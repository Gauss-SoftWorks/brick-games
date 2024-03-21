import pyray as pr  # type: ignore


class TitleScreen:
    def __init__(self, width: int, height: int, font: int = 72) -> None:
        self.width = width
        self.height = height
        self.font = font
        self.options_font = self.font * 3 // 8

    def get_width_position(self, text: str, font: int) -> int:
        """Get the width coordinate for text."""
        text_width = pr.measure_text(text, font)
        x_coord = (self.width - text_width) // 2
        return int(x_coord)

    def title_screen(self) -> None:
        """Initiate title screen."""
        pr.init_window(self.width, self.height, "Brick Games")

        # Get x coordinates for title and quit text
        title_coord = self.get_width_position("Brick Games", self.font)
        quit_coord = self.get_width_position("Press Q to Quit", self.options_font)
        continue_coord = self.get_width_position("Press C to Continue", self.options_font)

        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(pr.BLACK)
            pr.draw_text("Brick Games", title_coord, self.height // 4, self.font, pr.WHITE)
            pr.draw_text("Press C to Continue", continue_coord, self.height // 2, self.options_font, pr.BLUE)
            pr.draw_text("Press Q to Quit", quit_coord, self.height * 5 // 8, self.options_font, pr.VIOLET)

            if pr.is_key_down(81):
                # print("Q has been pressed")
                pr.close_window()
            pr.end_drawing()
        pr.close_window()
