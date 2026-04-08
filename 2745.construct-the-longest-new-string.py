#
# @lc app=leetcode id=2745 lang=python3
#
# [2745] Construct the Longest New String
#

# @lc code=start
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:

        w = min(x, y)
        x -= w
        y -= w

        print(f"AA:{x}, BB:{y}, AB:{z}, AABB:{w}")

        ans = z * 2 + w * 4

        if x > 0:            
            ans += 2

        if y > 0:            
            ans += 2

        return ans
# @lc code=end

x = 2
y = 5
z = 1

sol = Solution()
ans = sol.longestString(x, y, z)
print(ans)