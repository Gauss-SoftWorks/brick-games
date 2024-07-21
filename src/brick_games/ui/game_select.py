import pyray as pr  # type: ignore


class GameSelect:
    def __init__(self, game_list: list[str]) -> None:
        self.game_list = game_list
        self.state = 'title_screen'

    def create_game_select(self) -> None:
        game_state = 'game_select'
        pr.begin_drawing()
        pr.clear_background(pr.WHITE)
        pr.draw_text("Select Game", 100, 100, 32, pr.BLACK)
        pr.draw_text("Press b to go Title Screen", 100, 150, 32, pr.BLACK)
        pr.draw_text("Press q to Quit", 100, 200, 32, pr.BLACK)
        pr.end_drawing()
