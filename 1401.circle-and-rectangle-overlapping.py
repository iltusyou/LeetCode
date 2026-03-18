#
# @lc app=leetcode id=1401 lang=python3
#
# [1401] Circle and Rectangle Overlapping
#

# @lc code=start
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        def shortestDistance(center, p1, p2):            
            if p1 <= center and center <= p2:                
                return 0            
            return min( abs(p1-center), abs(p2-center) )
        
        a = shortestDistance(xCenter, x1, x2)
        b = shortestDistance(yCenter, y1, y2)

        print(a, b , radius, (a**2 + b **2), radius**2)
                                        
        return (a**2 + b **2) <= radius**2
# @lc code=end

# radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1

# radius = 1
# xCenter = 0
# yCenter = 0
# x1 = -1
# y1 = 0
# x2 = 0
# y2 = 1

sol = Solution()
ans = sol.checkOverlap(radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1)
print(ans)
