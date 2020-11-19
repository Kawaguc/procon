# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
from dijkstra import dijkstra


def main():
    v, e, r = map(int, input().split())
    adj = [[] for _ in range(v)]
    for _ in range(e):
        s, t, d = map(int, input().split())
        adj[s].append((d, t))
    dist = dijkstra(r, adj)
    for d in dist:
        if d == float("inf"):
            print("INF")
        else:
            print(d)


if __name__ == "__main__":
    main()
