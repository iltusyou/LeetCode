#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for index, value in enumerate(nums):
            if value in hash:
                return [hash[value], index]

            diff = target - value
            hash[diff] = index
                    
        
# @lc code=end

nums = [3,2,4]
target = 6

# nums = [3,3]
# target = 6

sol = Solution()
ans = sol.twoSum(nums, target)
print(ans)


