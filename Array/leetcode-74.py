class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        row = 0

        while start <= end:
            mid = (start + end) // 2

            if matrix[mid][-1] > target:
                if matrix[mid][0] <= target:
                    row = mid
                    break
                else:
                    end -= 1

            elif matrix[mid][-1] < target:
                start += 1
            
            else:
                return True

        if end < 0:
            row = 0
        elif start >= len(matrix):
            row = len(matrix) - 1
            
        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right -= 1
            else:
                left += 1

        return False