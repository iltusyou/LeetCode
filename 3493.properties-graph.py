#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self._fa = list(range(n))
        self.cc = n

    def find(self, x: int) -> int:
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])
        return self._fa[x]

    def merge(self, from_: int, to: int) -> None:
        x, y = self.find(from_), self.find(to)
        if x == y:
            return
                
        self._fa[x] = y
        self.cc -= 1

class Solution:   
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:        
        
        sets = list(map(set, properties)) 
        uf = UnionFind(len(properties))
        
        for i, x in enumerate(sets):
            for j, y in enumerate(sets[:i]):
                if len(x & y) >= k:
                    uf.merge(i, j)                
        return uf.cc
    
# @lc code=end

properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]]
k = 1

# properties = [[1,2,3],[2,3,4],[4,3,5]]
# k = 2

# properties = [[1,1],[1,1]]
# k = 2

# properties = [[1,1],[2,3],[1,3]]
# k = 1

# properties = [[1,1,2],[1,1,3]]
# k = 2

sol = Solution()
ans = sol.numberOfComponents(properties, k)
print(ans)
