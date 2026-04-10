#
# @lc app=leetcode id=2145 lang=python3
#
# [2145] Count the Hidden Sequences
#

# @lc code=start
from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        if len(differences) == 1:
            ans = max(upper - lower - abs(differences[0]) + 1, 0) 
            
            return ans

        

        s = [0]
        for d in differences:
            s.append(s[-1]+d)
                    
        max_val = max(s)
        min_val = min(s)


        print(max_val, min_val)

        ans = upper - lower - (max_val - min_val) + 1
        ans = max(ans, 0)
        return ans
    
# @lc code=end

sol = Solution()

# ans = sol.numberOfArrays(differences = [1,-3,4], lower = 1, upper = 6)
# ans = sol.numberOfArrays(differences = [3,-4,5,1,-2], lower = -4, upper = 5)
# ans = sol.numberOfArrays(differences = [4,-7,2], lower = 3, upper = 6)
# ans = sol.numberOfArrays(differences = [-40], lower = -46, upper = 53)
ans = sol.numberOfArrays(differences = [83702,-5216], lower = -82788, upper = 14602)

print(ans)