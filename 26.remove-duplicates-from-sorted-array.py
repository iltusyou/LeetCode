#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left, right = 0, 1
        n = len(nums)
        cnt = 1

        while right < n:
            if nums[right] > nums[left]:
                left += 1
                nums[left] = nums[right]
                cnt += 1

            right += 1
         
        return cnt

        
                    
# @lc code=end

nums = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()
ans = sol.removeDuplicates(nums)
print(ans)