#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#

# @lc code=start
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row_count = []
        col_count = []

        for row in grid:
            row_count.append(sum(row))

        for i in range(len(grid[0])):
            col = sum(row[i] for row in grid)
            col_count.append(col)

        ans = 0

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1 and (row_count[i] > 1 or col_count[j]>1):
                    ans += 1

        return ans
# @lc code=end

grid = [[1,0],[1,1]]

sol = Solution()
ans = sol.countServers(grid)
print(ans)