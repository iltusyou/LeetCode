#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
import bisect
from collections import defaultdict, deque
import heapq


class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        self.left_cnt = 0
        self.right_cnt = 0       
        self.delayed = defaultdict(int)

    def add(self, x):
        if self.left_cnt >= self.right_cnt:
            heapq.heappush_max(self.left, x)
            remove = heapq.heappop_max(self.left)
            heapq.heappush(self.right, remove)
            self.right_cnt += 1

        else:
            heapq.heappush(self.right, x)
            remove = heapq.heappop(self.right)                
            heapq.heappush_max(self.left, remove)
            self.left_cnt += 1

    def remove(self, x):
        self.delayed[x] += 1
        if self.left and x <= self.left[0]:
            self.left_cnt -= 1
    
        else:
            self.right_cnt -= 1

        self.rebalance()
        self.prune()
        
    
    def prune(self):
        while self.left and self.delayed[self.left[0]] > 0:
            x = heapq.heappop_max(self.left)
            self.delayed[x] -= 1

        while self.right and self.delayed[self.right[0]] > 0:
            x = heapq.heappop(self.right)
            self.delayed[x] -= 1

    def rebalance(self):        
        while self.left_cnt > self.right_cnt:
            heapq.heappush(self.right, heapq.heappop_max(self.left))
            self.right_cnt += 1
            self.left_cnt -= 1

        while self.right_cnt > self.left_cnt + 1:
            heapq.heappush_max(self.left, heapq.heappop(self.right))
            self.left_cnt += 1
            self.right_cnt -= 1


    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
     
        que = deque()    
        even = (k % 2 == 0)
        ans = []
        for i, x in enumerate(nums):            
            if i == 0:
                que.append(x)                
                self.right.append(x)
                self.right_cnt += 1

            else:
                self.add(x)
                que.append(x)

            if i >= k:
                r = que.popleft()
                self.remove(r)                                            

            if i >= k-1:
                if even:
                    med = (self.left[0] + self.right[0]) / 2
                else:
                    med = self.right[0]

                ans.append(med)         

            print(i, x, self.left, self.right, self.delayed, ans)
                                                                                                                                           
        return ans
    
# @lc code=end

# nums = [1,3,-1,-3,5,3,6,7]
# k = 3

# nums = [1]
# k = 1

nums = [9,7,0,3,9,8,6,5,7,6]
k = 2

nums = [5,-2,1,3,7,3,6,4,-1]
k = 3

sol = Solution()
ans = sol.medianSlidingWindow(nums, k)
print(ans)