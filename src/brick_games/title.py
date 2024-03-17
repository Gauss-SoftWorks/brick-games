import pyray as pr


class TitleScreen:
    def __init__(self) -> None:
        pass

    def print_title(self):
        print('Welcome to Brick Games!')
    
    def title_screen(self):
        '''Create a 640x480 title screen.'''
        # Create a 640x480 window because this is God's chosen resolution
        width = 640
        height = 480
        pr.init_window(width, height, "Brick Games")
        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(pr.WHITE)
            # TODO: Center text given the window width and height.
            pr.draw_text("Brick Games", 100, 100, 72, pr.BLACK)
            pr.draw_text("Press Q to Quit", 180, 350, 32, pr.VIOLET)
            # Check if Q (81) has been pressed
            if pr.is_key_down(81):
                print('Q has been pressed')
                pr.close_window()
            pr.end_drawing()
        pr.close_window()