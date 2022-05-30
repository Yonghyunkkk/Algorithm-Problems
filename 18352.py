from collections import deque
import sys

input = sys.stdin.readline

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [987654321 for _ in range(n+1)]

count = 0

queue = deque([x])
distance[x] = 0

while queue:

    temp = queue.popleft()

    for i in graph[temp]:
        if distance[i] == 987654321:
            distance[i] = distance[temp] + 1
            queue.append(i)

check = 0
for i in range(1,len(distance)):
    if i != x:
        if distance[i] == k:
            print(i)
            check += 1

if check == 0:
    print(-1)