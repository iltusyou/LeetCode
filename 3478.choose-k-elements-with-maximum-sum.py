#
# @lc app=leetcode id=3478 lang=python3
#
# [3478] Choose K Elements With Maximum Sum
#

# @lc code=start
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        t = [(i, x, nums2[i]) for i, x in enumerate(nums1)]
        sorted_t = sorted(t, key= lambda x:x[1])        
        sum_dic = {}
        h = []
        s = 0
        curr = 0

        for _, j, l in sorted_t:    
            if j > curr:
                curr = j
                sum_dic[j] = s        

            heapq.heappush(h, l)
            s+=l
            if len(h) > k:
                s -= heapq.heappop(h)       
                                                                    
        return [sum_dic[x] for x in nums1]
        
# @lc code=end

nums1 = [4,2,1,5,3]
nums2 = [10,20,30,40,50]
k = 2

# nums1 = [2,2,2,2]
# nums2 = [3,1,2,3]
# k = 1

sol = Solution()
ans = sol.findMaxSum(nums1, nums2, k)
print(ans)
