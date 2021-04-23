def prime_factorization(n):
    """
    素因数分解 O(√N)
    >>> prime_factorization(12)
    [2, 2, 3]
    >>> prime_factorization(120)
    [2, 2, 2, 3, 5]
    >>> prime_factorization(1)
    []
    >>> prime_factorization(2)
    [2]
    """

    i = 2
    ret = []
    while i * i <= n:
        while n % i == 0:
            ret.append(i)
            n //= i
        i += 1
    if n > 1:
        ret.append(n)
    return ret


def main():
    pass


if __name__ == "__main__":
    main()
