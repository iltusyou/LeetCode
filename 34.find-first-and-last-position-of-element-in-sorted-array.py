#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:                        
    def searchFirst(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        
        left, right = 1, len(nums)-1
       
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target and nums[mid-1] < target:
                return mid
            elif nums[mid] < target:
                left = mid + 1                
            else:
                right = mid -1

        return left if nums[left] == target else -1
    
    def searchLast(self, nums: List[int], target: int, first: int) -> int:
        n = len(nums)-1
        if nums[-1] == target:
            return n

        left, right = first, n-1

        while left < right:
            mid = left + (right - left)//2          
            if nums[mid] == target and nums[mid + 1] > target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left if nums[left] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        if not nums:
            return [-1, -1]

        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        first = self.searchFirst(nums, target)
        if first == -1:
            return [-1, -1]
        
        last = self.searchLast(nums, target, first)


        return [first, last]

# @lc code=end


# nums = [5,7,7,8,8,10]
# target = 8

nums = []
target = 0

sol = Solution()
ans = sol.searchRange(nums, target)
print(ans)