import semaine_01.exo_1_les_bases as lb


def test_nombre_entre_zero_et_cent():
    assert lb.nombre_entre_zero_et_cent(0) is True
    assert lb.nombre_entre_zero_et_cent(100) is True
    assert lb.nombre_entre_zero_et_cent(50) is True
    assert lb.nombre_entre_zero_et_cent(101) is False
    assert lb.nombre_entre_zero_et_cent(-1) is False
    assert lb.nombre_entre_zero_et_cent(101) is False


def test_multiple_deux_ou_cinq():
    assert lb.multiple_deux_ou_cinq(2) is True
    assert lb.multiple_deux_ou_cinq(5) is True
    assert lb.multiple_deux_ou_cinq(10) is True
    assert lb.multiple_deux_ou_cinq(3) is False
    assert lb.multiple_deux_ou_cinq(7) is False
    assert lb.multiple_deux_ou_cinq(11) is False


def test_table_multiplication():
    assert lb.table_multiplication(2) == [[1, 2], [2, 4]]
    assert lb.table_multiplication(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert lb.table_multiplication(1) == [[1]]
    assert lb.table_multiplication(4) == [
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [3, 6, 9, 12],
        [4, 8, 12, 16],
    ]


def test_adresse_courriel():
    assert lb.adresse_courriel("Alice,Bouchard,example.com") == \
        "alice.bouchard@example.com"
    assert lb.adresse_courriel("Bob,Marley,example.com") == \
        "bob.marley@example.com"
    assert lb.adresse_courriel("Charlie,Brown,example.com") == \
        "charlie.brown@example.com"


def test_nombres_pairs():
    def helper(foo):
        assert foo(10) == [0, 2, 4, 6, 8, 10]
        assert foo(5) == [0, 2, 4]
        assert foo(0) == [0]

    helper(lb.nombres_pairs_while)
    helper(lb.nombres_pairs_for)


def test_zip_listes():
    assert lb.zip_listes([1, 2, 3], ['a', 'b', 'c']) == \
        [(1, 'a'), (2, 'b'), (3, 'c')]
    assert lb.zip_listes([1, 2], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b')]
    assert lb.zip_listes([1, 2, 3], ['a', 'b']) == [(1, 'a'), (2, 'b')]
    assert lb.zip_listes([], []) == []
    assert lb.zip_listes([1], ['a']) == [(1, 'a')]
    assert lb.zip_listes([], [1, 2]) == []
    assert lb.zip_listes([1, 2], []) == []


def test_intersection_listes():
    assert lb.intersection_listes([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert lb.intersection_listes([1, 2, 3], [4, 5, 6]) == []
    assert lb.intersection_listes([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert lb.intersection_listes([], []) == []
    assert lb.intersection_listes([1, 2, 3], []) == []
    assert lb.intersection_listes([], [1, 2, 3]) == []


def test_intersection_listes_sans_doublons():
    assert lb.intersection_listes_sans_doublons([1, 2, 2, 3],
                                                [2, 3, 4]) == [2, 3]
    assert lb.intersection_listes_sans_doublons([1, 2, 3], [4, 5, 6]) == []
    assert lb.intersection_listes_sans_doublons([1, 2, 3],
                                                [1, 2, 3]) == [1, 2, 3]
    assert lb.intersection_listes_sans_doublons([], []) == []
    assert lb.intersection_listes_sans_doublons([1, 2, 3], []) == []
    assert lb.intersection_listes_sans_doublons([3], [1, 2, 3]) == [3]


def test_somme_liste():
    assert lb.somme_liste([1, 2, 3]) == 6
    assert lb.somme_liste([1, 2, 3, 4]) == 10
    assert lb.somme_liste([1, 2, 3, 4, 5]) == 15
    assert lb.somme_liste([1]) == 1
    assert lb.somme_liste([]) == 0
    assert lb.somme_liste([0]) == 0
    assert lb.somme_liste([0, 0, 0]) == 0