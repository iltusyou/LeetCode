#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        ans = sum( abs(x - y) for x, y in zip(seats, students))
        
        return ans
# @lc code=end

seats = [4,1,5,9]
students = [1,3,2,6]

sol = Solution()
ans = sol.minMovesToSeat(seats, students)
print(ans)