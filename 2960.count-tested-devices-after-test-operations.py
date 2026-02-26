#
# @lc app=leetcode id=2960 lang=python3
#
# [2960] Count Tested Devices After Test Operations
#

# @lc code=start
from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        m = 0
        for n in batteryPercentages:
            if n > m:
                m+=1

        return  m
        
# @lc code=end

# batteryPercentages = [1,1,2,1,3]
batteryPercentages = [0,1,2]

sol = Solution()
ans = sol.countTestedDevices(batteryPercentages)
print(ans)