#
# @lc app=leetcode id=2521 lang=python3
#
# [2521] Distinct Prime Factors of Product of Array
#

# @lc code=start
from typing import List, Tuple


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        MX = max(nums)+1
        lpf = [0] * MX
        for i in range(2, MX):
            for j in range(i, MX, i):
                if lpf[j] == 0:
                    lpf[j] = i

        def prime_factorization(x: int) -> List[Tuple[int, int]]:
            res = []
            while x > 1:
                p = lpf[x] 
                e = 1
                x //=p
                while x % p == 0:
                    e += 1
                    x //= p

                res.append((p, e))
            return res
            
        ans = set()
        for n in nums:
            pf = prime_factorization(n)
            for x in pf:
                ans.add(x[0])
        
        return len(ans)
    
# @lc code=end

nums = [2,4,3,7,10,6]
sol = Solution()
ans = sol.distinctPrimeFactors(nums)
print(ans)
