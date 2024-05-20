import pytest 

def calculer(a, b):
    return a + b, a - b, a * b

def test_calculer():
    resultat_attendu = (5, 1, 6)
    assert calculer(3, 2) == resultat_attendu