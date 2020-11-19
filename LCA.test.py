# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C
import sys

from LCA import LCA

sys.setrecursionlimit(10 ** 6)


def main():
    n = int(input())
    G = [[] for _ in range(n)]
    for i in range(n):
        c = list(map(int, input().split()))
        k = c[0]
        for j in range(k):
            G[i].append(c[j + 1])
    lca = LCA(G, 0)
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        print(lca.query(u, v))


if __name__ == "__main__":
    main()
