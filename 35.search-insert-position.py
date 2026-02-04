#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1        

        if nums[right] < target:
            return right + 1

        while left <= right:            
            mid = left +  (right - left) //2
            print(mid, left, right, nums[mid])

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1     
                
        return left
        
# @lc code=end

# nums = [1,3,5,6]
# target = 5

nums = [1,3,5,6]
target = 2
# Output: 1

sol = Solution()
ans = sol.searchInsert(nums, target)
print(ans)
