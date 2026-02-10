#
# @lc app=leetcode id=3583 lang=python3
#
# [3583] Count Special Triplets
#

# @lc code=start
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        dic1 = {}
        dic2 = {}

        res = 0
        mod = 10 ** 9 + 7

        for n in nums:
            
            if n%2 == 0 and n // 2 in dic2:
                res += dic2.get(n // 2)
                res %= mod        

            if 2 * n in dic1:
                dic2[n] = dic2.get(n, 0) + dic1[2 * n]

            dic1[n] = dic1.get(n, 0) + 1
                        
            print(dic1, dic2, res, n)

        return res
        
# @lc code=end

# nums = [6,3,6]
nums = [14,7,14,4,15,2]

sol = Solution()
ans = sol.specialTriplets(nums)
print(ans)