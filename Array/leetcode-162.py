class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        
        # for i in range(0, len(nums)):
        #     if i == 0:
        #         if nums[i] > nums[i+1]:
        #             return i
        #     elif i == len(nums) - 1:
        #         if nums[i] > nums[i-1]:
        #             return i
        #     elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if mid > 0 and nums[mid] < nums[mid-1]:
                right = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                return mid