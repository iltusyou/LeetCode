#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        left, right = 0, len(nums) - 1        

        while left <= right:            
            mid = left +  (right - left) //2
            print(mid, left, right, nums[mid])

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1     
                
        return -1
        
# @lc code=end

nums = [-1,0,3,5,9,12]
target = 9

# nums = [-1,0,3,5,9,12]
# target = 2



sol = Solution()
ans = sol.search(nums, target)
print(ans)