from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:        
        if len(nums) == 1:
            return 1
        
        if len(nums) == 2:
            return 2 if nums[0] != nums[1] else 1
                
        up = 0 #0, 1, -1
        count = 1
        
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            print(diff, up)
            if (diff > 0 and up <= 0): 
                count += 1
                up = 1

            if (diff < 0 and up >= 0):
                count +=1
                up = -1
            
        return count

# nums = [1,7,4,9,2,5] 
# nums = [1,17,5,10,13,15,10,5,16,8]
# nums = [0,0,0]
nums = [3,3,3,2,5]

sol = Solution()
ans = sol.wiggleMaxLength(nums)
print(ans)