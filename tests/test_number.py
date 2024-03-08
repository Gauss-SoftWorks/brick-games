from brick_games.main import number

def test_main():
    num = 42
    output = number(num)
    assert f"Your number is {num}." == output
