def sum_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:     
        return "ゼロで除算はできません。"

def power_numbers(a, b):
    return a ** b

def root_numbers(a, b):
    return a ** (1/b)

