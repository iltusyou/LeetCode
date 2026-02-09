#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        maxScore = values[0]-1
        res = values[0]
        print(maxScore)
        
        for i in range(1, len(values)):
            
            curr = maxScore + values[i]
            res = max(res, curr)          
                                  
            score = values[i] - 1
            if score >= maxScore:                
                maxScore = score       
            else:
                maxScore -= 1

            print(maxScore)
            
               
        return res
# @lc code=end

# values = [8,1,5,2,6]
# values = [1,2,2]
# values = [7,8,8,10]
values = [2,7,7,2,1,7,10,4,3,3]

sol = Solution()
ans = sol.maxScoreSightseeingPair(values)
print(ans)