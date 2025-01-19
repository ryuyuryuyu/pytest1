from . import calc
def test_sum_numbers():
    result = calc.sum_numbers(2, 3)
    assert result == 5
    
def test_subtract_numbers():
    result = calc.subtract_numbers(2, 3)
    assert result == -1

def test_multiply_numbers():
    result = calc.multiply_numbers(2, 3)
    assert result == 6

def test_divide_numbers():
    result = calc.divide_numbers(6, 3)
    assert result == 2
    
def test_divide_by_zero():
    result = calc.divide_numbers(6, 0)
    assert result == "ゼロで除算はできません。"

def test_power_numbers():
    result = calc.power_numbers(2, 3)
    assert result == 8
    
def test_root_numbers():
    result = calc.root_numbers(8, 3)
    assert result == 2