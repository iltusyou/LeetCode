#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hash = {
            '1':'',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqs',
            '8':'tuv',
            '9':'wxyz'
        }
          
        res = []

        def backtracking(d, path):            
            if len(d) == 0:
                res.append(path)
                return
            
            for c in hash[d[0]]:
                pathCopy = path + c
                backtracking(d[1:], pathCopy)
                                 
        digits = digits.replace('1','')        
        backtracking(digits,"")

        return res
        
# @lc code=end

digits = "123"
sol = Solution()
ans = sol.letterCombinations(digits)
print(ans)

