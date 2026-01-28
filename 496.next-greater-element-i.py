#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        hash = {}
        stack = []

        for n in nums2:            
            while len(stack)> 0 and stack[-1] < n:                    
                    hash[stack.pop()] = n
                
                                    
            stack.append(n)            


        print(hash)

        for i in range(len(nums1)):
            res.append(hash.get(nums1[i], -1))
                
        return res
        
# @lc code=end

# nums1 = [4,1,2]
# nums2 = [1,3,4,2]

# nums1 = [2,4]
# nums2 = [1,2,3,4]

# nums1 = [1,3,5,2,4]
# nums2 = [6,5,4,3,2,1,7]

nums1 = [4,1,2,0]
nums2 = [3,4,2,0,1]

sol = Solution()
ans = sol.nextGreaterElement(nums1, nums2)
print(ans)