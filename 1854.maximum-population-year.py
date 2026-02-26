#
# @lc app=leetcode id=1854 lang=python3
#
# [1854] Maximum Population Year
#

# @lc code=start

from typing import List
from itertools import accumulate

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        end = max(death for _, death in logs)        
        start = min(birth for birth, _ in logs)
        diff = [0] * (end - start + 1)

        print(start, end)
        for birth, death in logs:
            diff[birth - start] += 1
            diff[death - start] -= 1          


        pop_max = 0
        pop_max_index = 0

        prefix_sum = 0
        for i, x in enumerate(diff):
            prefix_sum += x

            if prefix_sum > pop_max:
                pop_max = prefix_sum
                pop_max_index = i

        ans = pop_max_index + start
        return ans
# @lc code=end

# logs = [[1950,1961],[1960,1971],[1970,1981]]
logs = [[2008,2026],[2004,2008],[2034,2035],[1999,2050],[2049,2050],[2011,2035],[1966,2033],[2044,2049]]

sol = Solution()
ans = sol.maximumPopulation(logs)
print(ans)
