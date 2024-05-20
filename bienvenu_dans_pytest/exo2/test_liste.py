import pytest

@pytest.fixture
def liste_vide():
    return []

def test_liste_vide_initialement(liste_vide):
    assert len(liste_vide) == 0


# peu importe le nombre après len(liste_vide) == "X" // pytest PASSE !!!