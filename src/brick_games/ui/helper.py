import pyray as pr  # type: ignore


def center_text_x(text: str, font_size: int) -> int:
    """Calculate x-coordinate to horizontally center text"""
    screen_width = pr.get_screen_width()
    text_width = pr.measure_text(text, font_size)
    xc = (screen_width - text_width) // 2
    return int(xc)
