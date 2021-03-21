def dijkstra(s, edges):
    """
    単一始点全点対最短路
    s: 始点
    edges: 隣接リストで(重み、頂点)のtupleを持つ
    """
    import heapq

    d = [float("inf")] * len(edges)
    d[s] = 0
    pq = [(0, s)]
    while pq:
        c, v = heapq.heappop(pq)
        if d[v] < c:
            continue
        for c2nv, nv in edges[v]:
            if c + c2nv < d[nv]:
                d[nv] = c + c2nv
                heapq.heappush(pq, (d[nv], nv))
    return d
