# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A
from procon.segtree import SegmentTree


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
