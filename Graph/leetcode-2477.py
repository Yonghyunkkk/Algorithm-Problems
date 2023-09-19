class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        res = 0

        graph = [[] for _ in range(n)]

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            nonlocal res
            passengers = 0

            for neigh in graph[node]:
                if parent != neigh:
                    p = dfs(neigh, node)
                    passengers += p
                    res += int(ceil(p / seats))

            return passengers + 1

        dfs(0, -1)
        return res