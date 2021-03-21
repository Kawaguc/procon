# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
from procon.warshall_floyd import warshall_floyd


def main():
    v, e = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    d = warshall_floyd(v, edges)
    for i in range(v):
        if d[i][i] < 0:
            print("NEGATIVE CYCLE")
            exit()
    for i in range(v):
        for j in range(v):
            if d[i][j] == float("inf"):
                d[i][j] = "INF"
        print(*d[i])


if __name__ == "__main__":
    main()
