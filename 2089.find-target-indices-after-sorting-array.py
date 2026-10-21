#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums)


        ans = [i for i, x in enumerate(sorted_nums) if x == target]
                
        return ans
    
# @lc code=end

# nums = [1,2,5,2,3]
# target = 2

nums = [1,2,5,2,3]
target = 5


sol = Solution()
ans = sol.targetIndices(nums, target)
print(ans)