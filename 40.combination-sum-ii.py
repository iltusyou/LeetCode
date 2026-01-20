#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List

class Solution:       

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:        
        if sum(candidates) < target:
            return []

        candidates.sort()
        n = len(candidates)        

        used = [0] * n
        res = []

        def backtracking(total, startIndex, path):          
            print(startIndex, path, total, used)    
   
            if total == target:                
                res.append(path[:])
                return                         
            
            
            for i in range(startIndex, len(candidates)):
                
                if i > startIndex and candidates[i] == candidates[i-1] and used[i] == 0:                               
                    continue

                if total + candidates[i]> target:
                    break
                
                
                total += candidates[i]
                path.append(candidates[i])
                used[i] = 1                     
                               
                backtracking(total , i+1, path)                

                total-=candidates[i]
                used[i] = 0                
                path.pop()

                                                                
        backtracking(0, 0, [])

        return res
# @lc code=end

candidates = [10,1,2,7,6,1,5]
target = 8

# candidates = [2,5,2,1,2]
# target = 5

# candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# target = 27

# candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# target = 30

sol = Solution()
ans = sol.combinationSum2(candidates, target)
print(ans)