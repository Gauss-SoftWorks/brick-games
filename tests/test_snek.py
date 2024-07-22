from brick_games.games import snek


def test_snek_hello() -> None:
    obj = snek.Snake()
    assert obj.hello() == "Hello"
