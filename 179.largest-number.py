#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from filecmp import cmp
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(n) for n in nums]
              
        key = cmp_to_key(lambda x,y:  int(y+x) - int(x+y))
        sorted_nums = sorted(str_nums, key = key)  

        ans = ''.join(sorted_nums)
        ans = str(int(ans))
              
        return ans
    
# @lc code=end

nums = [3,30,34,5,9]
sol = Solution()
ans = sol.largestNumber(nums)
print(ans)