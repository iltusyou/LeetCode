#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        resLen = len(nums)

        nums = nums + nums[0:-1]   
        res = [-1] * len(nums)     
        print(nums)

        stack = []
        
        for i in range(len(nums)):
            print(nums[i], stack, res)

            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                res[stack[-1]] = nums[i]
                stack.pop()
                
            stack.append(i)

        return res[0:resLen]
# @lc code=end

nums = [1,2,3,4,3]
sol = Solution()
ans = sol.nextGreaterElements(nums)
print(ans)