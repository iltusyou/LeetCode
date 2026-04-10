#
# @lc app=leetcode id=2766 lang=python3
#
# [2766] Relocate Marbles
#

# @lc code=start
from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        s = set()
        for n in nums:
            s.add(n)          

        for from_, to in zip(moveFrom, moveTo):
            s.remove(from_)
            s.add(to)
            
        ans = sorted(list(s))
     
        return ans
# @lc code=end



sol = Solution()
ans = sol.relocateMarbles(nums = [1,1,3,3], moveFrom = [1,3], moveTo = [2,2])


print(ans)
