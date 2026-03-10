#
# @lc app=leetcode id=3551 lang=python3
#
# [3551] Minimum Swaps to Sort by Digit Sum
#

# @lc code=start
from typing import List

class UnionFind:
    def __init__(self, n):
        self._fa = list(range(n))
        self._size = [1] * n
        self.cc = n

    def find(self, x):
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])
        return self._fa[x]
    
    def get_distinct(self):
        return list(set(self._fa))
    
    def get_size(self, x: int) -> int:        
        return self._size[self.find(x)]
    
    def merge(self, from_, to):
        x, y = self.find(from_), self.find(to)
        if x == y:
            return
        
        self._fa[x] = y
        self._size[y] += self._size[x]
        self.cc -= 1    

class Solution:    
    def minSwaps(self, nums: List[int]) -> int:
                
        a = sorted((sum(map(int, str(x))), x, i) for i, x in enumerate(nums)) 
                        
        n = len(nums)
        uf = UnionFind(n)
   
        for i, (_, _, j) in enumerate(a):
            uf.merge(i, j)  

        return n - uf.cc
    
# @lc code=end

# nums = [37,100]
# nums = [22,14,33,7]
# nums = [18,43,34,16]
nums = [62264880,357180177,17009883,257027582]

sol = Solution()
# ans = sol.minSwaps(nums)
# print(ans)
# print(int(str(37)))

i=15
print(i&-i)