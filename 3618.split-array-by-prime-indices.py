#
# @lc app=leetcode id=3618 lang=python3
#
# [3618] Split Array by Prime Indices
#

# @lc code=start
from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return abs(sum(nums))


        is_prime = [False] * 2 + [True] * (n - 2)
        primes = []

        prime_sum = 0
        not_prime_sum = nums[0] + nums[1]
        
        for i in range(2, n):            
            if is_prime[i]:
                primes.append(i)
                prime_sum += nums[i]

                for j in range(i*i, n, i):
                    is_prime[j] = False

            else:
                not_prime_sum += nums[i]

        return abs(prime_sum - not_prime_sum)
    
# @lc code=end

# nums = [2,3,4]
# nums = [-1,5,7,0]
nums = [-602741550,-243097563,435785956,-567926486,-462415908]


sol = Solution()
ans = sol.splitArray(nums)
print(ans)