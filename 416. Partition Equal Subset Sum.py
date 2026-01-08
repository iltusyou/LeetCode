from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)

        if nums_sum % 2 != 0:
            return False

        half = nums_sum / 2
        print(half)

        nums = sorted(nums)
        print(nums)


        return
    
nums = [1,5,11,5]
sol = Solution()
ans = sol.canPartition(nums)
print(ans)