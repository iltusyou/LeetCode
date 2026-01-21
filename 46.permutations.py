#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def backTracking(self, nums,  path, res, used):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(0, len(nums)):
            if used[i] == 1:
                continue

            path.append(nums[i])
            used[i] = 1
            self.backTracking(nums, path, res, used)
            path.pop()
            used[i] = 0

        return

    def permute(self, nums: List[int]) -> List[List[int]]:    
        res = []
        used = [0] * len(nums)
        self.backTracking(nums, [], res, used)    
        return res
        
# @lc code=end


nums = [1,2,3]
# nums = [1]

sol = Solution()
ans = sol.permute(nums)
print(ans)