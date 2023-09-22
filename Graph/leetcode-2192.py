class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        ancestors = [set() for _ in range(n)]
        indegree = [0] * n

        for parent, child in edges:
            indegree[child] += 1
            graph[parent].append(child)
            ancestors[child].add(parent)

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            parent = q.popleft()

            for child in graph[parent]:
                indegree[child] -= 1
                ancestors[child].update(ancestors[parent])

                if indegree[child] == 0:
                    q.append(child)

        return [sorted(l) for l in ancestors]