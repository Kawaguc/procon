def prime_factorization(n):
    """
    素因数分解 O(√N)
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
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(126) == [2, 3, 3, 7]
    assert prime_factorization(1) == []
    assert prime_factorization(2) == [2]


if __name__ == "__main__":
    main()
