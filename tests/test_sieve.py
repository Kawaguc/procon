from procon.sieve import Sieve


def test_Sieve():
    s = Sieve(30)
    assert not s.is_prime(1)
    assert s.is_prime(2)
    assert s.is_prime(3)
    assert not s.is_prime(4)
    assert s.is_prime(5)
    assert s.prime_factorization(5) == [5]
    assert s.prime_factorization(9) == [3, 3]
    assert s.prime_factorization(24) == [2, 2, 2, 3]
