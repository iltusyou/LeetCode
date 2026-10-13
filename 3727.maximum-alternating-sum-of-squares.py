#
# @lc app=leetcode id=3727 lang=python3
#
# [3727] Maximum Alternating Sum of Squares
#

# @lc code=start
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = [x * x for x in nums]        
        arr = sorted(arr, reverse = True)

        n = len(arr)        
        half = (int)((n+1)/2)

        ans = sum(arr[0:half]) - sum(arr[half:])
                
        return ans
    
# @lc code=end

# nums = [1,2,3]
# nums = [1,-1,2,-2,3,-3]

nums = [12,-4]

sol = Solution()
ans = sol.maxAlternatingSum(nums)
print(ans)