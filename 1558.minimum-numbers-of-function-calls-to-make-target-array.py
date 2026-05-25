#
# @lc app=leetcode id=1558 lang=python3
#
# [1558] Minimum Numbers of Function Calls to Make Target Array
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def getOp0(n: int) -> int:           
            binary_str = bin(n)[2:]
            cnt = binary_str.count('1')
            return cnt
        
        def getOp1(n: int) -> int:

            if n == 0 or n == 1:
                return 0

            p = 1
            while pow(2, p) <= n:
                p += 1
            return p - 1
                    
        ans = 0
        for n in nums:
            op0 = getOp0(n)
            ans += op0

        m = max(nums)
        op1 = getOp1(m)
        ans += op1

        return ans

        
# @lc code=end

# nums = [1,5]
# nums = [3,2,2,4]
# nums = [4,2,5]
# nums = [1000000000]
nums = [0]

sol = Solution()
ans = sol.minOperations(nums)
print(ans)

# print(sol.getMinOp0(1000000000))