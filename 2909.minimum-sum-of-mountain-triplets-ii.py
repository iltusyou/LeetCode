#
# @lc app=leetcode id=2909 lang=python3
#
# [2909] Minimum Sum of Mountain Triplets II
#

# @lc code=start
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        l = len(nums)        
        sums = [float('inf')] * l

        prefix_min = nums[0]
        for i in range(1, l-1):     
            if nums[i] > prefix_min:
                sums[i] = prefix_min

            if nums[i] < prefix_min:
                prefix_min = nums[i]            

        res = float('inf')
        suffix_min = nums[l-1]
        for i in range(l-2, -1, -1):
            if nums[i] > suffix_min and sums[i] != float('inf'):
                tmp = nums[i] + sums[i] + suffix_min 
                if tmp < res:
                    res = tmp
            
            if nums[i] < suffix_min:
                suffix_min = nums[i]            
            
        if res == float('inf'):
            res = -1                        

        return res
        
# @lc code=end


# nums = [5,4,8,7,10,2]
nums = [1,2,3,2]

sol = Solution()
ans = sol.minimumSum(nums)
print(ans)