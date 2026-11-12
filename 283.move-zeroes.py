#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        left, right = 0, 0

        while right < n:
            if nums[right] == 0:
                right += 1

            else:
                nums[left], nums[right] = nums[right], nums[left]
                right+=1
                left+=1
        
# @lc code=end

nums = [0,1,0,3,12]

sol = Solution()
ans = sol.moveZeroes(nums)
print(ans)