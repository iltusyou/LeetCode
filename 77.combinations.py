#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(i, arr):
            print(arr)
            if len(arr) == k:
                nonlocal res
                res.append(arr)                
            
            for j in range(i+1, n+1):
                arrCopy = arr.copy()
                arrCopy.append(j)      
                backtracking(j, arrCopy)
                                                                    
        backtracking(0, [])

        return res
# @lc code=end

n = 10
k = 2

sol = Solution()
ans = sol.combine(n, k)
print(ans)