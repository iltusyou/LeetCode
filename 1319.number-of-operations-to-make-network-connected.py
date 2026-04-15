#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        l = len(connections)
        if l < n-1:
            return -1
        
        done = [0] * l

        def dfs()

        return
    
# @lc code=end

n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]

sol = Solution()
ans = sol.makeConnected(n, connections)
print(ans)