#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
  
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0

        for x in s:
            if x == '(':
                low += 1
                high += 1
            elif x == ')':
                low -= 1
                high -= 1

                if high < 0:
                    return False
                
            else:
                low -= 1
                high += 1

            if low == -1:
                low = 0

        return low == 0

  

        

        

# @lc code=end

# s = "(*))"
# s = "("
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
# s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"

sol = Solution()
ans = sol.checkValidString(s)
print(ans)