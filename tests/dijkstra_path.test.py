# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
from procon.dijkstra_path import dijkstra_path, get_path


def main():
    n, m, s, t = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((c, b))
    dist, prev = dijkstra_path(s, adj)
    if dist[t] == float("inf"):
        print(-1)
        exit()
    path = get_path(t, prev)
    edge_num = len(path) - 1
    print(dist[t], edge_num)
    for i in range(edge_num):
        print(path[i], path[i + 1])


if __name__ == "__main__":
    main()
