#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start

from collections import defaultdict, deque
import heapq


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        deq = deque()        
        max_deq, min_deq = deque(), deque()
                
        ans = 0
        for x in nums:            
            deq.append(x)            

            while max_deq and max_deq[-1] < x:
                max_deq.pop()
            max_deq.append(x)

            while min_deq and min_deq[-1] > x:
                min_deq.pop()
            min_deq.append(x)

            while max_deq[0] - min_deq[0] > limit:
                remove = deq.popleft()

                if max_deq[0] == remove:
                    max_deq.popleft()

                if min_deq[0] == remove:
                    min_deq.popleft()

            ans = max(ans, len(deq))        
                                                    
        return ans
    
# @lc code=end

nums = [8,2,4,7]
limit = 4

sol = Solution()
ans = sol.longestSubarray(nums, limit)
print(ans)
