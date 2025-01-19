from src import code
def test_sum_numbers():
    result = code.sum_numbers(2, 3)
    assert result == 5
    
def test_subtract_numbers():
    result = code.subtract_numbers(2, 3)
    assert result == -1

def test_multiply_numbers():
    result = code.multiply_numbers(2, 3)
    assert result == 6

def test_divide_numbers():
    result = code.divide_numbers(6, 3)
    assert result == 2

def test_power_numbers():
    result = code.power_numbers(2, 3)
    assert result == 8
    
def test_root_numbers():
    result = code.root_numbers(8, 3)
    assert result == 2