class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size
        self.group_num = size
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
        self.group_num -= 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def group_count(self):
        return self.group_num
