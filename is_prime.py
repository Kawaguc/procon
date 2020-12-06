def is_prime(n):
    """
    素数判定 O(√N)
    """
    i = 2
    if n <= 1:
        return False
    while i ** 2 <= n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True


def main():

    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)


if __name__ == "__main__":
    main()
