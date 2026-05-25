#
# @lc app=leetcode id=2384 lang=python3
#
# [2384] Largest Palindromic Number
#

# @lc code=start
from collections import defaultdict


class Solution:
    def largestPalindromic(self, num: str) -> str:

        h = [0] * 10
        for n in num:
            h[int(n)] += 1

        print(h)

        ans = ''
        for i in range(9, 0, -1):
            cnt = h[i]//2

            if h[i] >= 2:
                c = str(i)
                ans += c * cnt
                h[i] -= cnt * 2


        if h[0] >= 2 and len(ans) > 0:
            cnt = h[0]//2
            ans += '0' * cnt
            h[0] -= cnt * 2


        for i in range(9, -1, -1):
            if h[i] > 0:
                ans = ans + str(i) + ans[::-1]
                return ans

        return ans + ans[::-1]
                
        
# @lc code=end

# num = "444947137"
# num = "00009"
num = "00001105"

sol = Solution()
ans = sol.largestPalindromic(num)
print(ans)