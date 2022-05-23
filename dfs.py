
def dfs(graph,x,y,visited):
    
    if graph[x][y] != 1 and visited[x][y] != True:
        visited[x][y] = True
    else:
        return 1

    # east,south,west,north
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            temp = dfs(graph,nx,ny,visited)
    return temp

n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))


visited = [[False] * m for _ in range(n)]

result = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] != True and graph[i][j] != 1:
            result += dfs(graph,i,j,visited)
            print(i,j)