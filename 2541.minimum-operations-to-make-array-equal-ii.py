#
# @lc app=leetcode id=2541 lang=python3
#
# [2541] Minimum Operations to Make Array Equal II
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if sum(nums1) != sum(nums2):
            return -1
                
        add, minute = 0, 0
        for x, y in zip(nums1, nums2):       
            if x == y:
                continue

            if k == 0 :
                return -1

            if (x - y) % k != 0:
                return -1
            
            op = (x-y) // k
            if op > 0:
                add += op
            else:
                minute += op * -1

        ans = add if add == minute else -1

        return ans
# @lc code=end

# nums1 = [4,3,1,4]
# nums2 = [1,3,7,1]
# k = 3

nums1 = [10,5,15,20]
nums2 = [10,10,15,15]
k = 0

sol = Solution()
ans = sol.minOperations(nums1, nums2, k)

print(ans)