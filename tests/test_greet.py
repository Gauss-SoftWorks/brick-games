from brick_games.main import greet

def test_main():
    output = greet()
    assert "Howdy!" == output
