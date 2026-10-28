#
# @lc app=leetcode id=3644 lang=python3
#
# [3644] Maximum K to Sort a Permutation
#

# @lc code=start
from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        DEFAULT = int('11111111111111111', 2) 
        ans = DEFAULT

        for i, x in enumerate(nums):
            if i != x:
                ans = ans & x                
        
        if ans == DEFAULT:
            return 0

        return ans
        
# @lc code=end

# nums = [0,1,3,2]
nums = [0,1,3,2,4] #2

sol = Solution()
ans = sol.sortPermutation(nums)
print(ans)