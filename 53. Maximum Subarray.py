from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_max = -float('inf')
        sum = 0
        for i in range(0, len(nums)):
            sum = sum + nums[i]
            if sum > sum_max:
                sum_max = sum
            
            if sum < 0:
                sum = 0
                        
        return sum_max
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
ans = sol.maxSubArray(nums)
print(ans)