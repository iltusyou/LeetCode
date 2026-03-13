#
# @lc app=leetcode id=1952 lang=python3
#
# [1952] Three Divisors
#

# @lc code=start
class Solution:
    def isThree(self, n: int) -> bool:
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        for p in primes:
            if p * p == n:
                return True
        
        return False
# @lc code=end

n = 4
sol = Solution()
ans = sol.isThree(n)
print(ans)