#
# @lc app=leetcode id=3723 lang=python3
#
# [3723] Maximize Sum of Squares of Digits
#

# @lc code=start
class Solution:        
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        quot = (int)(sum / 9)
        rem = sum % 9

        l = quot
        if rem > 0:
            l += 1

        if l > num:
            return ""

        print(quot, rem)

        ans = '9' * quot 

        if rem > 0:
            ans += str(rem)
        
        ans = ans + '0' * (num- len(ans))
        
        return ans
    
# @lc code=end

# num = 2
# sum = 3

# num = 2
# sum = 17

# num = 1
# sum = 10

# num = 1
# sum = 9

num = 2
sum = 19

sol = Solution()
ans = sol.maxSumOfSquares(num, sum)
print(ans)