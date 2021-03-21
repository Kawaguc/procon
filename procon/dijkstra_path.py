def dijkstra_path(s, edges):
    """
    単一始点全点対最短路
    s: 始点
    edges: 隣接リストで(重み、頂点)のtupleを持つ
    """
    import heapq

    d = [float("inf")] * len(edges)
    prev = [-1] * len(edges)
    d[s] = 0
    pq = [(0, s)]
    while pq:
        c, v = heapq.heappop(pq)
        if d[v] < c:
            continue
        for c2nv, nv in edges[v]:
            if c + c2nv < d[nv]:
                d[nv] = c + c2nv
                prev[nv] = v
                heapq.heappush(pq, (d[nv], nv))
    return d, prev


def get_path(t, prev):
    """
    dijkstra_pathで構築したprevと終点tから始点から終点までの最短路を構築して返す
    到達可能であることが前提
    """
    path = []
    while t != -1:
        path.append(t)
        t = prev[t]
    path.reverse()
    # path = path[::-1]
    return path
