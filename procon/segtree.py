from typing import Callable


class SegmentTree:
    def __init__(self, arr, operator: Callable, ide_ele):
        """
        arr: 元の配列
        operator: 関数
        ide_ele: 単位元
        """
        n = len(arr)
        num = 1 << (n - 1).bit_length()  # n以上の最小の2べき
        # bit_lengthの繰り上がりと最小の2べきの更新が1ずれている
        self.offset = num  # 元の0-indexedの配列とセグ木の配列(1-indexed)の葉のインデックスの差
        self.ide_ele = ide_ele
        self.operator = operator
        self.tree = [ide_ele] * (self.offset << 1)
        for i in range(n):
            self.tree[i + self.offset] = arr[i]
        # 構築
        for i in range(self.offset - 1, 0, -1):
            self.tree[i] = self.operator(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        元の配列のindexがkの値をxに更新
        """
        k += self.offset
        self.tree[k] = x
        while k > 1:  # 親が存在するなら
            # 偶数indexが左
            if k % 2 == 1:
                self.tree[k >> 1] = self.operator(self.tree[k ^ 1], self.tree[k])
            else:
                self.tree[k >> 1] = self.operator(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def get(self, i):
        return self.tree[i + self.offset]

    def query(self, l, r):
        """
        半開区間[l,r)のoperatorによる計算結果を得る
        """
        l += self.offset
        r += self.offset
        lret = self.ide_ele
        rret = self.ide_ele
        while l < r:
            if l & 1:
                lret = self.operator(lret, self.tree[l])
                l += 1
            if r & 1:
                rret = self.operator(self.tree[r - 1], rret)
            l >>= 1  # 親の階層へ移動
            r >>= 1
        return self.operator(lret, rret)


def main():
    n, q = map(int, input().split())
    a = [2 ** 31 - 1] * n
    ide_ele = 2 ** 31 - 1

    seg = SegmentTree(a, min, ide_ele)
    for _ in range(q):
        c, x, y = map(int, input().split())
        if c == 0:
            seg.update(x, y)
        if c == 1:
            print(seg.query(x, y + 1))


if __name__ == "__main__":
    main()
