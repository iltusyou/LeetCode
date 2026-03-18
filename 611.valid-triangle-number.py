#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def cnt(self, arr: List[int], target: int) -> int:        
        i = bisect.bisect_left(arr, target) 
        return i

    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)

        ans = 0

        for i in range(n-2):
            for j in range(i+1, n-1):
                s = nums[i] + nums[j]
                ans += self.cnt(nums[j+1:], s)
                        
        return ans

        

        
        
# @lc code=end

# nums = [2,2,3,4]
# nums = [7,0,0,0]
nums = [24,3,82,22,35,84,19]

sol = Solution()
ans = sol.triangleNumber(nums)
print(ans)