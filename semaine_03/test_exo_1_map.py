import semaine_03.exo_1_map as mp


def test_my_map():
    def double(x):
        return x * 2
    assert mp.my_map(double, [1, 2, 3]) == [2, 4, 6]
    assert mp.my_map(str, [1, 2, 3]) == ['1', '2', '3']
    assert mp.my_map(str, []) == []


def test_double_list():
    assert mp.double_list([1, 2, 3]) == [2, 4, 6]
    assert mp.double_list([]) == []


def test_str_list():
    assert mp.str_list([1, 2, 3]) == ['1', '2', '3']
    assert mp.str_list([]) == []
