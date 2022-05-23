from collections import deque

def bfs(graph,row,column,visited):
    queue = deque([(row,column)])
    visited[row][column] = True
    
    while queue:
        x,y = queue.popleft()

        # east,south,west,north
        dy = [1,0,-1,0]
        dx = [0,1,0,-1]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] != True:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))
    
visited = [[False] * m for _ in range(n)]

bfs(graph,0,0,visited)

print(graph[n-1][m-1])
