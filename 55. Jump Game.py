from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:        
        if len(nums) == 0: return 0

        cover = 0
        for i in range(0, len(nums)):            
            if i <= cover:
                cover = max(cover, i+nums[i])
                
            if cover >= len(nums) -1:
                return True

        return  False


# nums = [2,3,1,1,4] 
# nums = [3,2,1,0,4]
# nums = [1]
# nums = [2,0] True
nums = [1,2,3] #true

sol = Solution()
ans = sol.canJump(nums)
print(ans)