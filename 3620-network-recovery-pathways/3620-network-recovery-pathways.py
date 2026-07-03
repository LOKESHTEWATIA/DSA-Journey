from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        if not edges:
            return -1

        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v, c in edges:
            adj[u].append((v, c))
            indeg[v] += 1

        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []
        indeg2 = indeg[:]
        while q:
            u = q.popleft()
            topo.append(u)
            for v, c in adj[u]:
                indeg2[v] -= 1
                if indeg2[v] == 0:
                    q.append(v)

        costs = sorted(set(c for _, _, c in edges))
        INF = float('inf')

        def feasible(threshold):
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == INF or not online[u]:
                    continue
                du = dist[u]
                for v, c in adj[u]:
                    if c >= threshold and online[v]:
                        nd = du + c
                        if nd < dist[v]:
                            dist[v] = nd
            return dist[n - 1] <= k

        lo, hi, ans = 0, len(costs) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        return ans