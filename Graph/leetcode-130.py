class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Time Complexity = O(rows * cols)
            - This is because in worst case, when using DFS to traverse the board, every cell of the board may be visited once.
        """
        rows, cols = len(board), len(board[0])

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        def dfs(x, y):

            board[x][y] = 'T'

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'O':
                    dfs(nx, ny)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                        dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'