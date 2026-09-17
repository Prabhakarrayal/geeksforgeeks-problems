from typing import List
from heapq import heappush, heappop

class Solution:
    def minimumEdgeReversal(self, edges: List[List[int]], n: int, src: int, dst: int) -> int:

        if src == dst:
            return 0

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append((v, 0))
            adj[v].append((u, 1))

        dist = [float('inf')] * (n + 1)
        dist[src] = 0

        heap = [(0, src)]

        while heap:
            cost, u = heappop(heap)

            if cost > dist[u]:
                continue

            if u == dst:
                return cost

            for v, weight in adj[u]:
                new_cost = cost + weight

                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heappush(heap, (new_cost, v))

        return -1

