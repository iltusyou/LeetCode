#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List
from itertools import accumulate

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        diff = [0] * 20

        for start, end in intervals:
            diff[start] += 1
            diff[end+1] -= 1
        
        s = list(accumulate(diff, initial= 0))
        print(diff, s)

        res = []
        new = []

        for i, x in enumerate(s):
            if x > 0 and len(new) == 0:
                new.append(i-1)
            elif len(new) == 1 and x == 0:
                new.append(i-1)
                res.append(new.copy())
                new = []
                
        return res
        
# @lc code=end

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[5,6]]
intervals = [[1,4],[0,0]]

sol = Solution()
ans = sol.merge(intervals)
print(ans)
