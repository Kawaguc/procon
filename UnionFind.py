class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size
        # 親はその集合の大きさx(-1)
        # 子は親のindex

    def find(self, x):
        if self.data[x] < 0:
            return x
        parent = self.find(self.data[x])
        self.data[x] = parent
        return parent

    def size(self, x):
        return -self.data[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        # if self.data[x] > self.data[y]:
        if self.size(x) < self.size(y):
            x, y = y, x  # 集合として大きい方をx
        self.data[x] += self.data[y]
        self.data[y] = x
        return True

    def same(self, x, y):
        # return self.find(x) == self.find(y)
        return self.find(x) != self.find(y)


def main():
    # verified in https://judge.yosupo.jp/problem/unionfind
    # http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(q):
        t, u, v = map(int, input().split())
        if t == 0:
            uf.unite(u, v)
        elif t == 1:
            if uf.same(u, v):
                print(1)
            else:
                print(0)


if __name__ == "__main__":
    main()
