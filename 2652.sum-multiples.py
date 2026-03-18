#
# @lc app=leetcode id=2652 lang=python3
#
# [2652] Sum Multiples
#

# @lc code=start
class Solution:    
    def sumOfMultiples(self, n: int) -> int:

        def countMultiples(n, i):
            if n < i:
                return 0

            cnt = n//i
            return ( (1+cnt) * cnt // 2) * i 

        return countMultiples(n, 3) + countMultiples(n, 5) + countMultiples(n, 7) \
            - countMultiples(n, 15) - countMultiples(n, 21) - countMultiples(n, 35) \
            + countMultiples(n, 105)
    
# @lc code=end

n = 7
n = 15
sol = Solution()
ans = sol.sumOfMultiples(n)
print(ans)