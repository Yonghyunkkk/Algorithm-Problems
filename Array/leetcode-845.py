class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        mountain = 1
        is_mountain = 0

        for i in range(len(arr) - 1):
            if i == 0 and arr[i] >= arr[i+1]:
                continue
            elif arr[i] < arr[i+1]:
                if i > 0 and arr[i-1] > arr[i] and arr[i] < arr[i+1] and is_mountain > 0:
                    res = max(res, mountain)
                    is_mountain -= 1
                    mountain = 2
                else:
                    mountain += 1
            elif arr[i] > arr[i+1] and mountain > 1:
                mountain += 1
                is_mountain += 1
            elif arr[i] == arr[i+1]:
                if is_mountain > 0:
                    res = max(res, mountain)
                mountain = 1
        
        if is_mountain > 0:
            res = max(res, mountain)

        return res if res != 1 else 0