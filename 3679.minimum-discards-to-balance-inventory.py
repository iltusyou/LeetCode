#
# @lc app=leetcode id=3679 lang=python3
#
# [3679]  Minimum Discards to Balance Inventory
#

# @lc code=start
from typing import List


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        hash = {}
        ans = 0

        for i in range(len(arrivals)) :
            left = i - w
            if left >= 0:
                hash[arrivals[left]] = hash.get(arrivals[left], 0)-1

            hash[arrivals[i]] = hash.get(arrivals[i], 0) + 1

            if hash[arrivals[i]] > m and arrivals[i] != 0:
                hash[arrivals[i]] -= 1
                ans += 1
                arrivals[i] = 0
                            
            print(i, arrivals[i], hash, arrivals)
            
        return ans
# @lc code=end


# arrivals = [1,2,1,3,1]
# w = 4
# m = 2

# arrivals = [1,2,3,3,3,4]
# w = 3
# m = 2

# arrivals = [10,4,3,6,4,5,6,1,4]
# w = 7
# m = 1

arrivals = [8,8,8,1,7,4,3,7,5,2]
w = 7
m = 1

sol = Solution()
ans = sol.minArrivalsToDiscard(arrivals, w, m)
print(ans)
