import numpy as np
import semaine_02.exo_1_numpy as npy


def test_tableaux():
    assert np.array_equal(npy.tab1, np.array([]))
    assert np.array_equal(npy.tab2, np.zeros(20))
    assert np.array_equal(npy.tab3, np.ones(18))
    assert np.array_equal(npy.tab4, np.ones(3) * 10)
    assert len(npy.tab5) == 10
    assert np.all(npy.tab5 >= 0) and np.all(npy.tab5 <= 1)
    assert len(npy.tab7) == 3
    assert np.all(npy.tab7 >= 5) and np.all(npy.tab7 <= 10)
    assert np.array_equal(npy.tab8, np.zeros((4, 2)))
    assert np.array_equal(npy.tab9, np.ones((10, 5)))
    assert np.array_equal(npy.tab10, np.eye(6) * 10)
    assert np.array_equal(npy.tab11, np.arange(15, 101))
    assert np.array_equal(npy.tab12, np.arange(22, 80, 2))
    assert len(npy.tab13) == 100
    assert np.all(npy.tab13 >= 0) and np.all(npy.tab13 <= 5)


def test_statistiques_notes():
    notes = np.array([1, 2, 3, 3, 4, 5, 6])
    stats = npy.statistiques_notes(notes)
    assert np.isclose(stats['moyenne'], 3.42857143, atol=1e-6)
    assert np.isclose(stats['mediane'], 3)
    assert np.isclose(stats['ecart_type'], 1.590789, atol=1e-6)


def test_valeurs_X():
    assert np.array_equal(npy.valeurs_X(np.array([1, 2, 3, 2, 4]), 2),
                          np.array([1, 3]))
    assert np.array_equal(npy.valeurs_X(np.array([1, 2, 3, 4]), 5),
                          np.array([]))
    assert np.array_equal(npy.valeurs_X(np.array([]), 1), np.array([]))


def test_kilogramme_livre():
    assert np.allclose(npy.kilogramme_livre(np.array([0, 1, 2])),
                       np.array([0, 2.20462, 4.40924]), atol=1e-5)
    assert np.allclose(npy.kilogramme_livre(np.array([5])),
                       np.array([11.0231]), atol=1e-5)
    assert np.allclose(npy.kilogramme_livre(np.array([])),
                       np.array([]), atol=1e-5)


def test_valeurs_non_communes():
    assert np.array_equal(npy.valeurs_non_communes(np.array([1, 2, 3]),
                                                   np.array([3, 4, 5])),
                          np.array([1, 2, 4, 5]))
    assert np.array_equal(npy.valeurs_non_communes(np.array([1, 2, 3]),
                                                   np.array([1, 2, 3])),
                          np.array([]))
    assert np.array_equal(npy.valeurs_non_communes(np.array([]),
                                                   np.array([1, 2, 3])),
                          np.array([1, 2, 3]))
