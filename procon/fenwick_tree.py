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


def main():
    a = [1, 2, 3, 4, 5]
    ft = FenwickTree(len(a))
    for i in range(len(a)):
        ft.add(i, a[i])
    assert ft.sum(0, 5) == 15
    assert ft.sum(0, 6) == 15
    assert ft.sum(1, 5) == 14
    assert ft.sum(2, 5) == 12
    ft.add(4, 3)
    assert ft.sum(2, 5) == 15


def main2():
    # https://atcoder.jp/contests/practice2/tasks/practice2_b
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    ft = FenwickTree(n)
    for i, ai in enumerate(a):
        ft.add(i, ai)
    for _ in range(q):
        b, c, d = map(int, input().split())
        if b == 0:
            ft.add(c, d)
        else:
            print(ft.sum(c, d))


if __name__ == "__main__":
    main()
    # main2()
