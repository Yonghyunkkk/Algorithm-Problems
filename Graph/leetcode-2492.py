from collections import deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        res = int(1e9)
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n + 1)

        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        q = deque([1])
        visited[1] = True

        while q:
            v = q.popleft()

            for neigh, dist in graph[v]:
                res = min(res, dist)
                if not visited[neigh]:
                    q.append(neigh)
                    visited[neigh] = True
                
        return res