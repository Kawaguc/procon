# from is_prime import is_prime
from procon.is_prime import is_prime


def test_is_prime0():
    assert not is_prime(0)


def test_is_prime1():
    assert not is_prime(1)


def test_is_prime2():
    assert is_prime(2)


def test_is_prime3():
    assert is_prime(3)


def test_is_prime4():
    assert not is_prime(4)


def test_is_prime5():
    assert is_prime(5)
