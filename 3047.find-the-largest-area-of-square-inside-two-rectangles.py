#
# @lc app=leetcode id=3047 lang=python3
#
# [3047] Find the Largest Area of Square Inside Two Rectangles
#

# @lc code=start
from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)

        def area(b1, t1, l1, r1, b2, t2, l2, r2):
            b = max(b1, b2)
            t = min(t1, t2)
            l = max(l1, l2)
            r = min(r1, r2)

            y = t - b
            x = r - l

            if y <= 0 or x <= 0:
                return 0
            
            return min(x, y) ** 2
            

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                b1, l1 = bottomLeft[i]
                t1, r1 = topRight[i]
                b2, l2 = bottomLeft[j]
                t2, r2 = topRight[j]

                a = area(b1, t1, l1, r1, b2, t2, l2, r2)
                ans = max(ans, a)

                print(i, j, a)

        return ans
# @lc code=end

bottomLeft = [[1,1],[2,2],[3,1]]
topRight = [[3,3],[4,4],[6,6]]

sol = Solution()
ans = sol.largestSquareArea(bottomLeft, topRight)
print(ans)