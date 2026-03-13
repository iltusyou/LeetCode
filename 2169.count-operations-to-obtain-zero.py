#
# @lc app=leetcode id=2169 lang=python3
#
# [2169] Count Operations to Obtain Zero
#

# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        
        def gcd(a, b):
            ans = 0
            while a > 0:
                ans += b // a
                tmp = a
                a = b % a                
                b = tmp
            return ans
        
        ans = gcd(num1, num2)
           
        return ans
# @lc code=end

num1 = 10
num2 = 10

sol = Solution()
ans = sol.countOperations(num1, num2)
print(ans)