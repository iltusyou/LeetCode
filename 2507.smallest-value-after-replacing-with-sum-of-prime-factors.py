#
# @lc app=leetcode id=2507 lang=python3
#
# [2507] Smallest Value After Replacing With Sum of Prime Factors
#

# @lc code=start
from typing import List, Tuple


class Solution: 

    def smallestValue(self, n: int) -> int:        

        def get_prime_factors_sum(x:int) -> int:
            p, s = 2, 0
            while x > 1:
                while x % p == 0:                
                    s+=p
                    x //= p                
                p+=1
            return s
        
        
        ans = n
        while True:            
            n = get_prime_factors_sum(n)
            if ans == n:
                break
            ans = n

        return ans

    
# @lc code=end

n = 15
sol = Solution()
ans = sol.smallestValue(n)
print(ans)
