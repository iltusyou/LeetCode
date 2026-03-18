#
# @lc app=leetcode id=3074 lang=python3
#
# [3074] Apple Redistribution into Boxes
#

# @lc code=start
from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        capacity.sort(reverse = True)

        i = 0
        s = 0
        while s < total_apple:
            s += capacity[i] 
            i+=1

        return i
# @lc code=end

apple = [1,3,2]
capacity = [4,3,1,5,2]

sol = Solution()
ans = sol.minimumBoxes(apple, capacity)
print(ans)