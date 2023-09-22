class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0

        graph = [[] for _ in range(n)]
        visited = [False] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(v, parent):
            nonlocal edge_count, node_count
            visited[v] = True
            node_count += 1

            for neigh in graph[v]:
                edge_count += 1
                if not visited[neigh]:
                    dfs(neigh, parent)
 
        for node in range(n):
            edge_count = 0
            node_count = 0
            if not visited[node]:
                dfs(node, node)
                if node_count * (node_count - 1) == edge_count:
                    components += 1

        return components