from itertools import combinations
from collections import deque


global n
n = int(input())

board = []
teachers = []
students = []
spaces = []

for _ in range(n):
    board.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        elif board[i][j] == 'S':
            students.append((i,j))
        else:
            spaces.append((i,j))

#east,west,south,north
dx = [0,0,1,-1]
dy = [1,-1,0,0]
initial_index = []

for x,y in teachers:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:

            if i == 0:
                initial_index.append((nx,ny,"right"))
            elif i == 1:
                initial_index.append((nx,ny,"left"))
            elif i == 2:
                initial_index.append((nx,ny,"down"))
            else:
                initial_index.append((nx,ny,"up"))

for data in combinations(spaces,3):
    for x,y in data:
        board[x][y] = 'O'

    check = bfs(initial_index)

    if not check:
        print("NO")
        break
    else:
        for r,c in data:
            board[r][c] = 'X'

def bfs(initial_index):
    queue = deque(initial_index)

    while queue:
        x,y,direction = queue.popleft()

        if direction == "right":
            nx = x
            ny = y + 1
        elif direction == "left":
            nx = x
            ny = y - 1
        elif direction == "down":
            nx = x + 1
            ny = y
        elif direction == "up":
            nx = x
            ny = y - 1
        
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 'S':
                return False
            elif board[nx][ny] == 'O':
                return
            else:
                queue.append((nx,ny,direction))
    return True
