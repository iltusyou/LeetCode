#
# @lc app=leetcode id=1696 lang=python3
#
# [1696] Jump Game VI
#

# @lc code=start
from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        que = deque()
        que.append((0, nums[0]))

        for i in range(1, len(nums)):

            curr = que[0][1] + nums[i]

            while que and que[-1][-1] <= curr:
                que.pop()

            que.append((i, curr))

            if que and i - que[0][0] == k:
                que.popleft()      
 
        return que[-1][1]
    
# @lc code=end

nums = [1,-1,-2,4,-7,3]
k = 2

sol = Solution()
ans = sol.maxResult(nums, k)
print(ans)

