class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    '''
    Also have to include k in dp.
    This is because it we do not store k, at that certain position, the knight might have       different k for each same position.
    '''`
        dp = {}

        def backtrack(x, y, k):
            if x < 0 or x >= n or y < 0 or y >= n:
                dp[(x,y,k)] = 0
                return 0

            if k == 0:
                dp[(x,y,k)] = 1
                return 1

            if (x,y,k) in dp:
                return dp[(x,y,k)]

            total = (backtrack(x-1, y-2, k-1) 
                    + backtrack(x-2, y-1, k-1) 
                    + backtrack(x-2, y+1, k-1) 
                    + backtrack(x-1, y+2, k-1) 
                    + backtrack(x+1, y-2, k-1) 
                    + backtrack(x+2, y-1, k-1) 
                    + backtrack(x+2, y+1, k-1) 
                    + backtrack(x+1, y+2, k-1))

            dp[(x,y,k)] = total / 8
            return dp[(x,y,k)]
       
        return backtrack(row, column, k)
