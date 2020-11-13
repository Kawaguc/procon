# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_B
from bellmanford import bellman_ford


def main():
    v, e, r = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    dist, has_negative_cycle = bellman_ford(r, v, edges)
    if has_negative_cycle:
        print("NEGATIVE CYCLE")
        exit()
    for i in range(v):
        if dist[i] == float("inf"):
            print("INF")
        else:
            print(dist[i])


if __name__ == "__main__":
    main()
