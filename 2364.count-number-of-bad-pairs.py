#
# @lc app=leetcode id=2364 lang=python3
#
# [2364] Count Number of Bad Pairs
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(int)

        for i, x in enumerate(nums):
            dic[i - x] += 1

        good_pairs_cnt = sum((v * (v-1)) // 2 for _, v in dic.items() if v > 1)
        all_cnt = (n * (n-1)) // 2

        ans = all_cnt - good_pairs_cnt
        
        return ans
        

        
        
# @lc code=end

# nums = [4,1,3,3]
nums = [1,2,3,4,5]

sol = Solution()
ans = sol.countBadPairs(nums)
print(ans)