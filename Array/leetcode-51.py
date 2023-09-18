class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        neg_diag = set()
        pos_diag = set()

        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                puzzle = ["".join(row) for row in board]
                res.append(puzzle)
                return

            for c in range(n):
                if c in cols or (r - c) in neg_diag or (r + c) in pos_diag:
                    continue

                cols.add(c)
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                cols.remove(c)
                neg_diag.remove(r-c)
                pos_diag.remove(r+c)
                board[r][c] = "."

        backtrack(0)

        return res