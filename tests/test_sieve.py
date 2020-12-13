from sieve import sieve_eratosthenes


def test_sieve_erathosthenes():
    assert sieve_eratosthenes(6) == [False, False, True, True, False, True, False]
