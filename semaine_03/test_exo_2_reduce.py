import semaine_03.exo_2_reduce as red


def test_my_reduce():
    def add(x, y):
        return x + y
    assert red.my_reduce(add, [1, 2, 3]) == 6
    assert red.my_reduce(add, [1]) == 1
    assert red.my_reduce(add, []) == 0


def test_sum_list():
    assert red.sum_list([1, 2, 3]) == 6
    assert red.sum_list([1]) == 1
    assert red.sum_list([]) == 0


def test_prod_list():
    assert red.prod_list([1, 2, 3]) == 6
    assert red.prod_list([1]) == 1
    assert red.prod_list([]) == 1


def test_max_list():
    assert red.max_list([1, 2, 3]) == 3
    assert red.max_list([1]) == 1
    assert red.max_list([]) is None


def test_my_map():
    def double(x):
        return x * 2
    assert red.my_map(double, [1, 2, 3]) == [2, 4, 6]
    assert red.my_map(str, [1, 2, 3]) == ['1', '2', '3']
    assert red.my_map(str, []) == []
