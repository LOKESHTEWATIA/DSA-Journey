from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))
        
        visited = [False] * (n + 1)
        min_score = float('inf')
        queue = deque([1])
        visited[1] = True
        
        while queue:
            city = queue.popleft()
            for neighbor, dist in graph[city]:
                min_score = min(min_score, dist)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return min_score