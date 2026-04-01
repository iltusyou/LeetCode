#
# @lc app=leetcode id=2335 lang=python3
#
# [2335] Minimum Amount of Time to Fill Cups
#

# @lc code=start
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:

        ans = 0
        s = sum(amount)
        while s > 1 and len([n for n in amount if n >0]) >=2:
            amount.sort( reverse= True)
            amount[0]-=1
            amount[1]-=1
            ans +=1
            s = sum(amount)
            print(amount)

        ans += s       

        return ans
# @lc code=end

# amount = [1,4,2]
amount = [5,0,0]

sol = Solution()
ans = sol.fillCups(amount)
print(ans)