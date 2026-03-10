#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [False] * 2 + [True] * (n-2)
        primes = []

        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
                for j in range(i*i, n, i):                    
                    is_prime[j] = False            
        
        return len(primes)
        
# @lc code=end

n = 10
sol = Solution()
ans = sol.countPrimes(n)
print(ans)