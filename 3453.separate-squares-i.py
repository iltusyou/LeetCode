#
# @lc app=leetcode id=3453 lang=python3
#
# [3453] Separate Squares I
#

# @lc code=start
from typing import List
from itertools import pairwise
from collections import defaultdict

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        diff = defaultdict(int)

        total_area = 0
        for _, y, l in squares:
            total_area += l ** 2
            diff[y] += l
            diff[y+l] -= l

        
        sorted_diff = sorted(diff)
        print(diff, sorted_diff, total_area)

        sum_l, area = 0, 0
        for y, y2 in pairwise(sorted_diff):
            sum_l += diff[y]
            area += sum_l * (y2-y)
            print(y, y2, sum_l, area, total_area / 2)

            if area *2 >= total_area:
                print('find')
                              
                return y2 - (area * 2 - total_area) / (sum_l * 2)
                            
        return
        
# @lc code=end

# squares = [[0,0,1],[2,2,1]]
# squares = [[0,0,2],[1,1,1]]
# squares = [[20,21,3],[28,29,3]]
squares = [[0,1000000000,1000000]]

sol = Solution()
ans = sol.separateSquares(squares)
print(ans)
