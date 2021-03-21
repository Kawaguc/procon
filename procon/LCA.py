class LCA:
    """
    最小共通祖先を求める
    G:隣接リスト
    root:根
    """

    def __init__(self, G, root):
        """
        O(nlogn)
        """
        V = len(G)
        K = 1
        while (1 << K) < V:
            K += 1
        self.parent = [[-1] * V for _ in range(K)]
        self.depth = [-1] * V
        self._dfs(G, root, -1, 0)
        for k in range(K - 1):
            for v in range(V):
                if self.parent[k][v] == -1:
                    self.parent[k + 1][v] = -1
                else:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]

    def _dfs(self, G, v, p, d):
        self.parent[0][v] = p
        self.depth[v] = d
        for nv in G[v]:
            if nv == p:
                continue
            self._dfs(G, nv, v, d + 1)

    def query(self, u, v):
        """
        O(logn)
        2頂点のLCAを求める
        """
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        K = len(self.parent)
        # 深さを揃える
        for k in range(K):
            if (self.depth[u] - self.depth[v]) >> k & 1:
                u = self.parent[k][u]
        if u == v:
            return u
        # 移動先が初めて一致しない時のその移動先の祖先がLCA
        for k in range(K - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]
