#
# @lc app=leetcode id=2897 lang=python3
#
# [2897] Apply Operations on Array to Maximize Sum of Squares
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:

        dic = defaultdict(int)

        for x in nums:
            b = bin(x)
            b = b.replace('0b', '')

            n = len(b)

            for i in range(n):
                if b[i] == '1':
                    dic[n-1-i] += 1

        # print(f"{dic}")

        ans = 0
        for i in range(k):
            a = sum([2 ** key for key in dic.keys() if dic[key] > i])
            ans += a**2

        MOD = 10**9 + 7
        ans = ans % MOD
        return ans
    
# @lc code=end

nums = [2,6,5,8]
k = 2

sol = Solution()
ans = sol.maxSum(nums, k)
print(ans)
