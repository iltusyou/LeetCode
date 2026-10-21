#
# @lc app=leetcode id=2913 lang=python3
#
# [2913] Subarrays Distinct Element Sum of Squares I
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:        
        ans = 0        
        n = len(nums)
        
        for l in range(n):            
            s = set()
            
            s.add(nums[l])
            cnt = 1

            ans += 1

            for r in range(l+1, n):
                if nums[r] not in s:
                    s.add(nums[r])
                    cnt += 1

                ans += cnt ** 2            

        return ans         
        
    
# @lc code=end

nums = [1,2,1]

sol = Solution()
ans = sol.sumCounts(nums)
print(ans)
