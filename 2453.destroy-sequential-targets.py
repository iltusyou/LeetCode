#
# @lc app=leetcode id=2453 lang=python3
#
# [2453] Destroy Sequential Targets
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        dic = defaultdict(list)
        for n in nums:
            dic[n%space].append(n)

        mx = ans = 0
        for a in dic.values():
            m, low = len(a), min(a)
            if m > mx or (m == mx and low < ans):
                mx, ans = m, low
            
        return ans        
    
# @lc code=end

# nums = [3,7,8,1,1,5]
# space = 2

# nums = [1,3,5,2,4,6]
# space = 2

nums = [1,5,3,2,2]
space = 10000

sol = Solution()
ans = sol.destroyTargets(nums, space)
print(ans)