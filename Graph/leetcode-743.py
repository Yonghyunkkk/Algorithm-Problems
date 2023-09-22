import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        distance = [int(1e9)] * (n + 1)
        res = 0

        for a, b, time in times:
            graph[a].append((b, time))

        q = []

        heapq.heappush(q, (k, 0))
        distance[k] = 0

        while q:
            v, dist = heapq.heappop(q)

            if distance[v] < dist:
                continue

            for neigh, cost in graph[v]:
                if dist + cost < distance[neigh]:
                    distance[neigh] = dist + cost
                    heapq.heappush(q, (neigh, dist + cost))

        for i in range(1, n + 1):
            if distance[i] == int(1e9):
                return -1
            res = max(res, distance[i])
        return res