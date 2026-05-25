#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        find_a, find_b, find_c = False, False, False
        target_a, target_b, target_c = target

        for t in triplets:
            a, b, c = t
            if a > target_a or b > target_b or c > target_c:
                continue

            if a == target_a:
                find_a = True

            if b == target_b:
                find_b = True

            if c == target_c:
                find_c = True

            if find_a and find_b and find_c:
                return True                            

        return False
# @lc code=end

triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]

sol = Solution()
ans = sol.mergeTriplets(triplets, target)
print(ans)
