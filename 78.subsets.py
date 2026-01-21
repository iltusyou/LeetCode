#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def backTracking(self, nums, path, res):       
        res.append(path[:])
        
        for i in range(0, len(nums)):
            print(i)
            path.append(nums[i])
            self.backTracking(nums[i+1:], path, res)
            path.pop()


    def subsets(self, nums: List[int]) -> List[List[int]]:        

        res = []
        self.backTracking(nums, [], res)
        return res
        
# @lc code=end

nums = [1,2,3]
sol = Solution()
ans = sol.subsets(nums)
print(ans)