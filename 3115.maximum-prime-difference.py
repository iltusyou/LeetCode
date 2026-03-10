#
# @lc app=leetcode id=3115 lang=python3
#
# [3115] Maximum Prime Difference
#

# @lc code=start
from math import isqrt
from typing import List

def is_prime(n: int) -> bool:    
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
        
    return n >= 2
   
class Solution:                       
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        i = 0
        while nums[i] not in prime:
            i+=1

        j = len(nums) - 1
        while nums[j] not in prime:
            j -= 1        

        return j - i
    
# @lc code=end

# nums = [4,2,9,5,3]
# nums = [4,8,2,8]
# nums = [2,2]
nums = [1,7]

sol = Solution()
ans = sol.maximumPrimeDifference(nums)
print(ans)
