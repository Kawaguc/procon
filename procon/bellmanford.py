def bellman_ford(s, n, edges):
    """
    単一始点最短路の長さを求める
    O(EV)
    """
    has_negative_cycle = False
    d = [float("inf")] * n
    d[s] = 0
    for i in range(n):
        update = False
        for frm, to, cost in edges:
            if d[to] > d[frm] + cost:
                d[to] = d[frm] + cost
                update = True
        if not update:
            break
        if i == n - 1:
            has_negative_cycle = True  # 頂点数と同じ数だけ辺を眺めてもまだ距離の更新が行われているので負の閉路が存在
            return d, has_negative_cycle
    return d, has_negative_cycle


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
