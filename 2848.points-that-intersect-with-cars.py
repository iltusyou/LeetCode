#
# @lc app=leetcode id=2848 lang=python3
#
# [2848] Points That Intersect With Cars
#

# @lc code=start
from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key= lambda x:x[0])            
        curr = nums[0]
        ans = 0

        print(nums)

        for i in range(1, len(nums)):
            if nums[i][0] <= curr[1]:
                end = max(curr[1], nums[i][1])
                curr = [curr[0], end]
            else:
                ans += curr[1] - curr[0] + 1
                curr = nums[i]
                        
        ans += curr[1] - curr[0] + 1

        return ans
    
# @lc code=end

nums = [[3,6],[1,5],[4,7]]
# nums = [[1,3],[5,8]]
# nums = [[4,4],[9,10],[9,10],[3,8]]

sol = Solution()
ans = sol.numberOfPoints(nums)
print(ans)