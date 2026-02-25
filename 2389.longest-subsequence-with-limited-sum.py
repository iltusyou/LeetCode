#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#

# @lc code=start
from typing import List
from itertools import accumulate
import bisect


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:        
        nums.sort()
        prefix_sum = list(accumulate(nums, initial=0))

        ans = []
        for q in queries:
            i = bisect.bisect_left(prefix_sum, q)

            if i >= len(prefix_sum) or prefix_sum[i] > q:
                i -= 1

            ans.append(i)
            
        return ans
# @lc code=end

# nums = [4,5,2,1]
# queries = [3,10,21]

nums = [2,3,4,5]
queries = [1]

sol = Solution()
ans = sol.answerQueries(nums, queries)
print(ans)