#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)):            
            while len(stack) > 0 and temperatures[i] >  temperatures[stack[-1]]:
                removeIndex = stack.pop()        
                res[removeIndex] = i - removeIndex
            
            stack.append(i)
            
        return res
# @lc code=end

temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
ans = sol.dailyTemperatures(temperatures)
print(ans)