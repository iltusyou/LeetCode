#
# @lc app=leetcode id=2615 lang=python3
#
# [2615] Sum of Distances
#

# @lc code=start
from typing import List
from itertools import accumulate

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * l
        d={}
        for i in range(len(nums)):
            
            k = nums[i]
            if k in d:
                d[k].append(i)
            else:
                d[k] = [i]

        for k in d.keys():
            arr = d[k]
            arr_len = len(arr)
            if arr_len == 1:
                continue

            prefix_sum = list(accumulate(arr, initial = 0)) 
            print(arr, prefix_sum)

            for i in range(arr_len):

                left =  i * arr[i] - prefix_sum[i]
                right = (prefix_sum[-1] - prefix_sum[i+1]) - arr[i] * (arr_len-1-i)
                ans[arr[i]] = left + right                
                       
        return ans
# @lc code=end

nums = [1,3,1,1,2]
sol = Solution()
ans = sol.distance(nums)
print(ans)