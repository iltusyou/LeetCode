from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:        
        maxReach = nums[0]
        for i in range(1, len(nums)):            
            if i <= maxReach:
                j = i + nums[i]                
                if j > maxReach:
                    maxReach = j            

        return True if maxReach >= len(nums) -1 else False


# nums = [2,3,1,1,4] 
# nums = [3,2,1,0,4]
# nums = [1]
# nums = [2,0] True
nums = [1,2,3] #true

sol = Solution()
ans = sol.canJump(nums)
print(ans)