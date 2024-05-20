import pytest

def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b


def test_diviser_par_zero():
    with pytest.raises(ValueError):
        diviser(8, 0)