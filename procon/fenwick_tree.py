class FenwickTree:
    """
    0-indexed
    """

    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def add(self, i, x):
        """
        0-indexed
        """
        i += 1
        while i <= self.n:
            self.data[i - 1] += x
            i += i & -i

    def sum(self, l, r):
        """
        0-indexed
        [l:r)
        """
        return self._sum(r) - self._sum(l)

    def _sum(self, i):
        """
        [0:r)
        """
        s = 0
        while i > 0:
            s += self.data[i - 1]
            i -= i & -i
        return s
