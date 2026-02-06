#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
from typing import List


class Solution:
    def findFirstPos(self, nums: List[int]) -> int:
        if nums[0] > 0:
            return 0
        
        if nums[-1] == 0:
            return len(nums)

        left, right = 0, len(nums) -1

        while left < right:
            mid = left + (right - left) // 2          
            if nums[mid] > 0 and nums[mid-1] <= 0:
                return mid

            elif nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1

        return left 
    
    def findLastNeg(self, nums:List[int]) -> int:
        if nums[-1] < 0:
            return len(nums) - 1
        
        if nums[0] == 0:
            return -1

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2          
            if nums[mid] < 0 and nums[mid+1] >= 0:
                return mid
            elif nums[mid] >= 0:
                right = mid - 1                 
            else:
                left = mid + 1

        return left

        

    def maximumCount(self, nums: List[int]) -> int:
        firstPos = self.findFirstPos(nums)

        lastPos = -1
        if firstPos > 0:
            lastPos = self.findLastNeg(nums)

        pos = len(nums) - firstPos
        neg = lastPos + 1

        ans = max(pos, neg)

        return ans
        
# @lc code=end

# nums = [-2,-1,-1,1,2,3]
# nums = [-3,-2,-1,0,0,1,2]
# nums = [5,20,66,1314]
nums = [0,0]

sol = Solution()

print(sol.findFirstPos(nums), sol.findLastNeg(nums))
ans = sol.maximumCount(nums)
print(ans)