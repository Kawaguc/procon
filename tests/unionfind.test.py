# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
import sys

from procon.unionfind import UnionFind

input = sys.stdin.buffer.readline


def main():
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
