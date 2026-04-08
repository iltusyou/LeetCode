#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#

# @lc code=start
from itertools import pairwise
from typing import List


class Solution:
    def dfs(self, arr: List, s:int, target: int) -> int:
        n = len(arr)
        print(arr, s, target)

        if s == target or n == 1:
            return arr[-1]

        if s > target:
           
            m = target // n
            print(n, m)
            ans = m if target - m * n <= (m+1) * n - target else m + 1
            if ans < arr[0]:
                return ans
        
        return self.dfs(arr[1:], s-arr[0], target - arr[0])

    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        s = sum(arr)

        ans = self.dfs(arr, s, target)
        return ans

        
        
            
# @lc code=end

# arr = [4,9,3]
# target = 10

# arr = [2,3,5]
# target = 10

# arr = [1547,83230,57084,93444,70879]
# target = 71237

arr = [2,3,5]
target = 11

sol = Solution()
ans = sol.findBestValue(arr, target)
print(ans)