#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#

# @lc code=start
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self._fa = list(range(n))
        self.cc = n
        
    def find(self, x):
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])
        return self._fa[x]
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def merge(self, from_, to):
        x, y = self.find(from_), self.find(to)
        if x == y:
            return
        self._fa[x] = y
        print(self._fa)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)

        def idx(c):
            return ord(c) - ord('a')

        for eq in [eq for eq in equations if eq[1] == '=']:
            uf.merge(idx(eq[3]), idx(eq[0]))
               
        for eq in [eq for eq in equations if eq[1] == '!']:
            if uf.is_same(idx(eq[3]), idx(eq[0])):
                return False                            

        return True
# @lc code=end

# equations = ["a==b","b!=a"]
equations = ["b==a","a==b"]

sol = Solution()
ans = sol.equationsPossible(equations)
print(ans)