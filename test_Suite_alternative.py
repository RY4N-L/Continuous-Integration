from test_function import add_numbers

def test_addition():
    assert add_numbers(4, 5) == 9

def test_addition_negative_numbers():
    assert add_numbers(-2, 7) == 5

def test_addition_float_numbers():
    assert round(add_numbers(1.5, 2.5), 2) == 4