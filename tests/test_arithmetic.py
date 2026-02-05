from simplemath import Calculator, Accumulator

def test_calculator_add():
    c = Calculator()
    assert c.add(2, 3) == 5

def test_divide_by_zero():
    c = Calculator()
    try:
        c.divide(1, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        assert True

def test_accumulator():
    a = Accumulator(10)
    assert a.add(5) == 15
    a.reset()
    assert a.total == 0.0
