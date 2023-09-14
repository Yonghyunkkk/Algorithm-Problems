class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start_word = word[0]

        rows, cols = len(board), len(board[0])

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        def dfs(x, y, idx):
            visited[x][y] = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and board[nx][ny] == word[idx]:
                    if idx == len(word) - 1:
                        return True

                    if dfs(nx, ny, idx + 1):
                        return True
                    else:
                        visited[nx][ny] = False

            return False
        

        for r in range(rows):
            for c in range(cols):
                visited = [[False] * cols for _ in range(rows)]
                if board[r][c] == start_word:
                    if len(word) == 1:
                        return True
                    
                    if dfs(r, c, 1):
                        return True
        return False
                    