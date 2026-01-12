#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n
        for i in range(0, n-1):
            if ratings[i] < ratings[i+1]:
                res[i+1] =  res[i] + 1

        print(res)

        for i in range(n-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                res[i-1] = max(res[i] + 1, res[i-1]) 

        s = sum(res)
        print(res)

        return s
# @lc code=end


# ratings = [1,0,2]
# ratings = [1,3,2,2,1]
# 7

ratings = [1,2,87,87,87,2,1]
# 13

ratings = [1,3,4,5,2]
# 11

sol = Solution()
ans = sol.candy(ratings)
print(ans)
