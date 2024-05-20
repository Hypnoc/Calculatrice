import pytest

def ajout (a, b):
    c = a + b
    return c


@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (1, 1, 2),
    (5, 4, 9),
])


def test_ajout(a, b, expected):
    assert ajout(a, b) == expected