#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left < right:
            mid = left + (right - left) // 2
            print(left, right, mid, letters[mid])

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left] if letters[left] > target else letters[0]
        
# @lc code=end

letters = ["c","f","j"]
target = "a"

# letters = ["c","f","j"]
# target = "c"

# letters = ["x","x","y","y"]
# target = "z"

sol = Solution()
ans = sol.nextGreatestLetter(letters, target)
print(ans)
