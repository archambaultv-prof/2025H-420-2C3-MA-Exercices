import semaine_03.exo_3_filter_list_comprehension as ex3


def test_my_filter():
    def is_even(x):
        return x % 2 == 0
    assert ex3.my_filter(is_even, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert ex3.my_filter(is_even, [1, 3, 5]) == []
    assert ex3.my_filter(is_even, []) == []


def test_even_list():
    assert ex3.even_list([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert ex3.even_list([1, 3, 5]) == []
    assert ex3.even_list([]) == []


def test_bar():
    assert ex3.bar([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_foo():
    assert ex3.foo([1, 2, 3, 4, 5, 6]) == [3, 5, 7]
    assert ex3.foo([1, 3, 5]) == [3, 5, 7]
    assert ex3.foo([]) == []


def test_baz():
    assert ex3.baz([1, 2, 3]) == [0, 0, 1, 0, 1, 2]
    assert ex3.baz([0, 1, 2]) == [0, 0, 1]
    assert ex3.baz([]) == []


def test_qux():
    assert ex3.qux([1, 2, 3]) == [0, 1]
    assert ex3.qux([1, 2, 3, 4, 5]) == [0, 1, 0, 2, 1, 3]
    assert ex3.qux([]) == []
