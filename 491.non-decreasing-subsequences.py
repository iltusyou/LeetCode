#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
from typing import List


class Solution:
    def backtTracking(self, nums, startIndex, path, res):                                                                              
        if len(path) >= 2:
            res.append(path[:])

        if startIndex >= len(nums):
            return                        
   
        used = set()
        for i in range(startIndex, len(nums)):
            
            # print(startIndex, i, path, used)

            if (len(path) > 0 and nums[i] < path[-1]) or (nums[i] in used):
                continue

            used.add(nums[i])                        
            
            path.append(nums[i])
            self.backtTracking(nums, i+1, path, res)
            path.pop()

        return

    def findSubsequences(self, nums: List[int]) -> List[List[int]]: 
        res = []
        
        self.backtTracking(nums, 0, [], res)

        return res
        
# @lc code=end


# nums = [4,6,7,7]
# nums = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]
nums = [-100,-100,0,0,0,100,100,0,0]

sol = Solution()
ans = sol.findSubsequences(nums)
print(ans)