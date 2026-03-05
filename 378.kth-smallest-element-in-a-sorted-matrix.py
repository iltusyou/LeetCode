#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start

from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []

        for row in matrix:            
            for x in row:
                heapq.heappush_max(h, x)
                if len(h) > k:
                    heapq.heappop_max(h)

        return heapq.heappop_max(h)
# @lc code=end

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

sol = Solution()
ans = sol.kthSmallest(matrix, k)
print(ans)

