from itertools import combinations
from collections import deque

def spread_virus(n,m,row,column,graph):
    # east,south,west,north
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    
    queue = deque([(row,column)])
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 1:
                continue

            else:
                graph[nx][ny] = 2
                queue.append((nx,ny))

def find_space(n,m,graph):
    total = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                total += 1

    return total

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

virus = []
empty = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i,j))

        elif graph[i][j] == 0:
            empty.append((i,j))

spaces = list(combinations(empty,3))
result = 0

for space in spaces:
    for x,y in space:
        graph[x][y] = 1
    
    for i,j in virus:
        spread_virus(n,m,i,j,graph)

    temp = find_space(n,m,graph)

    if temp > result:
        result = temp

    for x,y in space:
        graph[x][y] = 0

print(result)