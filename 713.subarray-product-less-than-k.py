#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 0
        
        n = len(nums)
        left, right = 0, 0
        p = 1
        ans = 0
        while right < n:
            p *= nums[right]
            
            while p >= k and left <=right :                
                p/=nums[left]
                left += 1

            ans += right - left + 1
            right += 1                                    
            # print(left, right, p, ans)

        return ans
# @lc code=end

# nums = [10,5,2,6]
# k = 100

nums = [1,2,3]
k = 0

# nums = [2]
# k = 1

sol = Solution()
ans = sol.numSubarrayProductLessThanK(nums, k)
print(ans)