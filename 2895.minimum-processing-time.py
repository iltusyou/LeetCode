#
# @lc app=leetcode id=2895 lang=python3
#
# [2895] Minimum Processing Time
#

# @lc code=start
from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse= True)

        ans = max(x + tasks[i*4] for i, x in enumerate(processorTime))

        return ans
# @lc code=end

processorTime = [8,10]
tasks = [2,2,3,1,8,7,4,5]

sol = Solution()
ans = sol.minProcessingTime(processorTime, tasks)
print(ans)