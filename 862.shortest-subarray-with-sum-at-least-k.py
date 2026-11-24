#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        
        prefix_sum = 0
        que = deque()
        que.append((-1, 0))
        
        ans = float('inf')

        for i, x in enumerate(nums):
            prefix_sum += x            

            while que and prefix_sum - que[0][1] >= k:
                idx, _ = que.popleft()
                ans = min(ans, i-idx)

            while que and prefix_sum <= que[-1][1]:
                que.pop()
                        
            que.append((i, prefix_sum))                                                

            # print(que)
            
        if ans == float('inf'):
            ans = -1

        return ans
# @lc code=end

nums = [1]
k = 1
#1

# nums = [1,2]
# k = 4

# nums = [2,-1,2]
# k = 3

# nums = [0,0,69,56,-34]
# k = 91
#2

sol = Solution()
ans = sol.shortestSubarray(nums, k)
print(ans)
