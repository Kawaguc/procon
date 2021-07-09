def is_prime(n):
    """
    素数判定 O(√N)
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
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
