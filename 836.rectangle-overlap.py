#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2  

        return not (a1 >= x2 or a2 <= x1) and not (b1 >= y2 or b2 <= y1)
# @lc code=end

# rec1 = [0,0,2,2]
# rec2 = [1,1,3,3]

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]

# rec1 = [0,0,1,1]
# rec2 = [2,2,3,3]

sol = Solution()
ans = sol.isRectangleOverlap(rec1, rec2)
print(ans)
