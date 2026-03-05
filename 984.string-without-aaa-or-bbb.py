#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#

# @lc code=start
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        if a == b:
            return 'ab' * a
                
        m, l, mstr, lstr = a, b, 'a', 'b'
        if b > a:
            m, l, mstr, lstr = b, a, 'b', 'a'

        remain = m-l
        
        t2 = min(remain, l) #連續出現2次的次數
        t1 = l - t2 #連續出現1次的次數
        tail = remain - l #尾部剩餘次數
        
        ans = (mstr + mstr + lstr) * t2 + (mstr + lstr) * t1 + mstr * tail
        
        return ans
# @lc code=end

a = 4
b = 1

# a = 2
# b = 3

sol = Solution()
ans = sol.strWithout3a3b(a, b)
print(ans)