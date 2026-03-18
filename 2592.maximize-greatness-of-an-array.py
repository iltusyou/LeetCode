#
# @lc app=leetcode id=2592 lang=python3
#
# [2592] Maximize Greatness of an Array
#

# @lc code=start
from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1


        cnt_max = max( val for val in dic.values())
        
        ans = len(nums) - cnt_max

        return ans
# @lc code=end

# nums = [1,3,5,2,1,3,1]
nums = [42,8,75,28,35,21,13,21]

sol = Solution()
ans = sol.maximizeGreatness(nums)
print(ans)