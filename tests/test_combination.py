from procon.combination import Combination

c = Combination()


def test_combination1():
    assert c(4, 2) == 6


def test_combination2():
    assert c(5, 2) == 10


def test_combination3():
    assert c(0, 0) == 1


def test_combination4():
    assert c(1, 0) == 1


def test_combination5():
    assert c(1, 1) == 1


def test_combination6():
    assert c(1, 2) == 0
