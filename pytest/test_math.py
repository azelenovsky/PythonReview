from re import X


def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def increment(x):
    return x + 1

def test_add():
    assert add(1,2) == 3
