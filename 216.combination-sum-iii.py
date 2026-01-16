#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtracking(k, n, i, path):   
            # print(i, path)

            if len(path) == k and sum(path) == n:
                res.append(path.copy())
                return
            
            
            for j in range(i, 10):
                path.append(j)                                
                backtracking(k,n,j+1,path)
                path.pop()             
        
        backtracking(k,n,1,[])
        return res
    
# @lc code=end

# k = 3
# n = 7

k = 3
n = 9

sol = Solution()
ans = sol.combinationSum3(k, n)
print(ans)