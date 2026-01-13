#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from typing import List
from collections import deque



class Solution:
    def keepMax(self, que:deque, num:int) -> deque:
        while que and que[-1] < num:
            que.pop()

        que.append(num)
        return que


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        que = deque()

        for i in range(0, k):
            que = self.keepMax(que, nums[i])
        
        res.append(que[0])
        
        for i in range(k, len(nums)):
            remove = nums[i-k]
            
            if remove == res[-1]:
                que.popleft()

            que = self.keepMax(que, nums[i])
            res.append(que[0])

            
            print(que, res)

        print(que)
            
    
        return
# @lc code=end


nums = [1,3,-1,-3,5,3,6,7]
k = 3

sol = Solution()
ans = sol.maxSlidingWindow(nums, k)