from greet import greet


def test_greet():
    assert greet("Saher") == "Hello, Saher!"


def test_greet_strips_spaces():
    assert greet("  Saher  ") == "Hello, Saher!"
