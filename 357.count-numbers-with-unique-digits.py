#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start

class Solution:

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def cnt(n: int) -> int:

            if n == 1:
                return 10
            
            p = 1
            for i in range(n-1):
                p *= (9 - i)        

            p *= 9

            return p 
        
        if n == 0:
            return 1
        
        ans = 0
        for i in range(1, n+1):
            ans += cnt(i)
                                           
        return ans
# @lc code=end

n = 2
sol = Solution()
ans = sol.countNumbersWithUniqueDigits(n)
print(ans)

