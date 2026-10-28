from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:        
        n = len(nums)

        if n == 1:
            return 0
        
        id0 = nums.index(0)
        id1 = nums.index(1)          

        if id1 - id0 == 1 or id0 - id1 == n-1:
            
            m = id0 - n
            for i in range(n):                
                if nums[i+ m] != i:
                    return -1                    
            
            return min(id0, n-id0+2) 
  
        elif id1 - id0 == -1 or id1 - id0 == n-1: 

            for i in range(n):
                if nums[id0 - i] != i:
                    return -1                      

            return min(id0+2, n-id0)
            
        else:
            return -1                    
            

# nums = [0,2,1]
# nums = [1,0,2]
nums = [1,2,3,0]

sol = Solution()
ans = sol.minOperations(nums)
print(ans)