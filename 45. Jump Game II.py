from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        minSteps = [float('inf')] * n
        minSteps[0] = 0
        
        for i in range(0, n):
            
            t = min(n-i-1, nums[i]) + 1

            for j in range(1, t):
                minSteps[i+j] = min(minSteps[i+j], minSteps[i] + 1) 
                

                            
        return minSteps[-1]
    

# nums = [2,3,1,1,4] #2
nums = [2,3,0,1,4] #2

sol = Solution()
ans = sol.jump(nums)
print(ans)