#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#

# @lc code=start
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        sortedNums = sorted(nums)       
        n = len(nums)
        i = 0
        while k>0 and i<n:
            if sortedNums[i] >= 0:
                break

            sortedNums[i] = sortedNums[i] * -1
            k-=1
            i+=1

        sortedNums = sorted(sortedNums)       
        print(sortedNums, k, i)

        k = k%2
        if k==1:            
            sortedNums[0] = sortedNums[0] * -1

 
        result = sum(sortedNums)
        return result
        
# @lc code=end


# nums = [4,2,3], k = 1
# nums = [2,-3,-1,5,-4], k = 2
# nums = [-100,-100,-100], k = 4
sol = Solution()
ans = sol.largestSumAfterKNegations(nums = [-100,-100,-100], k = 4)
print(ans)