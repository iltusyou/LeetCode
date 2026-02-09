#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}

        for n in nums:            
            hash[n] = hash.get(n, 0) + 1

        res = 0
        for k in hash.keys():
            value = hash[k]
            if value > 1:    
                res += value * (value-1)/2            

        return int(res)
# @lc code=end

nums = [1,2,3,1,1,3]
sol = Solution()
ans = sol.numIdenticalPairs(nums)
print(ans)