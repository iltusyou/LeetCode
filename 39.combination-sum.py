#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtracking(idx, path):                        
            print(idx, path)

            if sum(path) == target:
                res.append(path)
                return 
            
            if sum(path) > target:
                return

            i = idx

            while i < n:            

                pathCopy = path.copy()
                pathCopy.append(candidates[i])
                pathSum = sum(pathCopy)

                if pathSum > target:
                    break
   
                backtracking(i, pathCopy)
                i += 1

            return
        
        backtracking(0, [])

        return res
# @lc code=end

# candidates = [2,3,6,7]
# target = 7

candidates = [8,7,4,3]
target = 11

sol = Solution()
ans = sol.combinationSum(candidates, target)
print(ans)

