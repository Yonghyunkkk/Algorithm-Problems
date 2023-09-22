class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        value = [0] * n
        edges = [[0, i] for i in range(n)]
        res = 0

        for a, b in roads:        
            edges[a][0] += 1
            edges[b][0] += 1

        edges.sort()

        for i in range(n):
            value[edges[i][1]] = i + 1

        for a, b in roads:
            res += value[a] + value[b]

        return res