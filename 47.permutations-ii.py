#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List


class Solution:
    def backTracking(self, nums,  path, res, used):       
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(0, len(nums)):
           
            if used[i-1] == True and i > 0 and nums[i] == nums[i-1]:
                continue
           
            if used[i] == True:
                continue
                  
            path.append(nums[i])            
            used[i] = True
            self.backTracking(nums, path, res, used)
            path.pop()
            used[i] = False

        return

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        self.backTracking(nums, [], res, used)    
        return res
        
# @lc code=end

# nums = [1,1,2]
nums = [3,3,0,3]

sol = Solution()
ans = sol.permuteUnique(nums)
print(ans)

