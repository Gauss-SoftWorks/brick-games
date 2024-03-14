from brick_games.games.poong import Pong

def test_hello() -> None:
    obj = Pong()
    output = obj.hello()
    assert output == "Hello"
