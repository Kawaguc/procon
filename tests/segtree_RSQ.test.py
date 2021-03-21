# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B
from procon.segtree import SegmentTree


def main():
    n, q = map(int, input().split())
    ide_ele = 0
    a = [ide_ele] * (n + 1)

    def operator(a, b):
        return a + b

    seg = SegmentTree(a, operator, ide_ele)
    for _ in range(q):
        c, x, y = map(int, input().split())
        if c == 0:
            cur = seg.query(x, x + 1)
            seg.update(x, cur + y)
        if c == 1:
            print(seg.query(x, y + 1))


if __name__ == "__main__":
    main()
