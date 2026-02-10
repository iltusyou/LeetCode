#
# @lc app=leetcode id=1814 lang=python3
#
# [1814] Count Nice Pairs in an Array
#

# @lc code=start
from typing import List


class Solution:
    def rev(self, num: int) -> int:
        res = 0
        while num > 0:
            tmp = num % 10            
            res = res * 10 + tmp            
            num = num // 10                  
        return res

    def countNicePairs(self, nums: List[int]) -> int:        
        freq = {}
        for n in nums:                        
            key = n - self.rev(n)             
            freq[key] = freq.get(key, 0) + 1
            
        print(freq)

        res = 0
        mod = 10 ** 9 + 7

        for key in freq.keys():
            count = freq[key]            
            res += count * (count-1) // 2            
            res = res % mod             

        return int(res)
        
# @lc code=end

# nums = [42,11,1,97]
nums = [13,10,35,24,76, 120]

sol = Solution()
ans = sol.countNicePairs(nums)
print(ans)

# i = 49340344500
# j = 276887723

# ri = sol.rev(i)
# print(ri)
# rj = sol.rev(j)

# print(f"{i} + {rj} = {i + rj}")
# print(f"{j} + {ri} = {j + ri}")