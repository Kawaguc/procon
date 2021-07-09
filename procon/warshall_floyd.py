def warshall_floyd(v, edges):
    """
    v: 頂点数
    edges: (s,t,d)のタプルのリスト
    全点対最短路長を求める
    O(V^3)
    """

    dist = [[float("inf")] * v for _ in range(v)]
    for i in range(v):
        dist[i][i] = 0
    for s, t, d in edges:
        dist[s][t] = d
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
