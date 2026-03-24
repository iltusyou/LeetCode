#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        # nums2.sort()

        sorted_nums2 = sorted([(x, i) for i, x in enumerate(nums2)]) 

        # print(nums1, nums2, sorted_nums2)

        n = len(nums1)
        i, j, ans = 0, 0, [-1] * n
        rest = []

        while i < n:                        
            val, idx = sorted_nums2[j]
         
            if nums1[i] > val:   
                ans[idx] = nums1[i]              
                j+=1
            else:
                rest.append(nums1[i])
                            
            i+=1
   
        rest_idx = [i for i, x in enumerate(ans) if x == -1]

        for x, i in zip(rest, rest_idx):
            ans[i] = x


        return ans
        
# @lc code=end

# nums1 = [2,7,11,15]
# nums2 = [1,10,4,11]

nums1 = [12,24,8,32]
nums2 = [13,25,32,11]

sol = Solution()
ans = sol.advantageCount(nums1, nums2)
print(ans)