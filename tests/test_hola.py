from brick_games.main import hola

def test_main():
    output = hola()
    assert "hola" == output
