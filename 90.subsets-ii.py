#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from typing import List


class Solution:
    def backTracking(self, nums, path, startInex, res, used):
        print(path, used)

        res.append(path[:])

        for i in range(startInex, len(nums)):
            if i > startInex and nums[i] == nums[i-1] and used[i] == False:
                continue

            path.append(nums[i])
            used[i] = True
            self.backTracking(nums, path, i+1, res, used)
            path.pop()
            used[i] = False

        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        used = [False] * len(nums)
        
        self.backTracking(nums, [], 0, res, used)

        return res
# @lc code=end

# nums = [1,2,2]
# nums = [0]
nums = [4,4,4,1,4] 
#[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

sol = Solution()
ans = sol.subsetsWithDup(nums)
print(ans)