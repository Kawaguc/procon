def sieve_eratosthenes(n):
    """
    >>> table = sieve_eratosthenes(6)
    >>> table
    [False, False, True, True, False, True, False]
    >>> table[2]
    True
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False
    return is_prime


if __name__ == "__main__":
    import doctest

    doctest.testmod()
