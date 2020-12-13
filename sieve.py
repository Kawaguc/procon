def sieve_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False
    return is_prime


def test_sieve_erathosthenes():
    assert sieve_eratosthenes(6) == [False, False, True, True, False, True, False]


if __name__ == "__main__":
    test_sieve_erathosthenes()
