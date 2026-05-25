#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        d = defaultdict(list)

        for i, x in enumerate(nums):
            d[x].append(i)
          
        ans = []
        for q in queries:
            if len(d[nums[q]]) == 1:
                ans.append(-1)

            else:
                a = d[nums[q]]
                l = len(a)
                i = bisect_left(a, q)
                                
                if i == 0:
                    left = n - a[-1] + a[0]
                else:
                    left = a[i] - a[i-1]

                if i == l-1:
                    right = n - a[-1] + a[0]
                else:
                    right = a[i+1] - a[i]

                
                print(q, nums[q], d[nums[q]], i, left, right)

                distance = min(left, right)
                ans.append(distance)                

        return ans
# @lc code=end

nums = [1,3,1,4,1,3,2]
queries = [0,3,5]

sol = Solution()
ans = sol.solveQueries(nums, queries)
print(ans)