#
# @lc app=leetcode id=1175 lang=python3
#
# [1175] Prime Arrangements
#

# @lc code=start
from math import factorial


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        is_prime = [False] *2 + [True] * (n-1)
        primes = []

        for i in range(2, n+1):
            if is_prime[i]:
                primes.append(i)

                for j in range(i*i, n+1, i):                    
                    is_prime[j] = False


        primes_cnt = len(primes)        

        MOD = 10_000_000_07
        ans = factorial(primes_cnt) * factorial(n - primes_cnt) % MOD
    
        return ans
# @lc code=end

n = 100
sol = Solution()
ans = sol.numPrimeArrangements(n)
print(ans)