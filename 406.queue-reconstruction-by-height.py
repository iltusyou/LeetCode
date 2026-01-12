#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:      
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        res = []

        for i in range(0, len(people)):        
            res.insert(people[i][1], people[i])
            print(res)
  
        return res
        
# @lc code=end

# people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

sol = Solution()
ans = sol.reconstructQueue(people)
print(ans)
