class Sieve:
    def __init__(self, MAXN):
        """
        構築O(NloglogN)
        osa_k法
        """
        self.min_factor = [0] * (MAXN + 1)  # 最小の素因数を格納
        for i in range(MAXN + 1):
            self.min_factor[i] = i
        i = 2
        while i * i <= MAXN:
            if self.min_factor[i] == i:
                j = i * i
                while j <= MAXN:
                    if self.min_factor[j] > i:
                        self.min_factor[j] = i
                    j += i
            i += 1

    def is_prime(self, n) -> bool:
        """
        素数判定 O(1)
        >>> s = Sieve(100)
        >>> s.is_prime(3)
        True
        >>> s.is_prime(4)
        False
        """
        if n <= 1:
            return False
        else:
            return self.min_factor[n] == n

    def prime_factorization(self, n):
        """
        素因数分解O(logN)
        >>> s = Sieve(100)
        >>> s.prime_factorization(24)
        [2, 2, 2, 3]
        """
        res = []
        while n > 1:
            res.append(self.min_factor[n])
            n //= self.min_factor[n]
        return res


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
