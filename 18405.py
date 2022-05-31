from collections import deque

def virus(queue,type):
    length = len(queue)
    count = 0

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    if length == 0:
        return queue
    else:
        while count < length:
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = type
                        queue.append((nx,ny))
            count += 1
    return queue

global n

n,k = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

data = [[] for _ in range(k+1)]
records = [[] for _ in range(k+1)]
count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data[graph[i][j]].append((i,j))
            records[graph[i][j]].append((i,j))
            count += 1


for i in range(s):
    for j in range(1,len(data)):
        for k in range (len(data[j])):
            if i == 0:
                queue = deque([(data[j][k][0],data[j][k][1])])
                queue = virus(queue,j)
                records[j][k] = queue
                
            else:
                queue = virus(records[j][k],j)
                records[j][k] = queue

print(graph[x-1][y-1])