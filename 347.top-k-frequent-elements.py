#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}

        for n in nums:
            numsMap[n] = numsMap.get(n, 0) + 1

        indexMap = {}
        for key, value in numsMap.items():
            arr = indexMap.get(value, [])
            arr.append(key)
            indexMap[value] = arr

        res = []

        for key, value in  sorted(indexMap.items(), reverse = True):
            res.extend(value)            
            if len(res) >= k:
                break

        return res
        
# @lc code=end

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

sol = Solution()
ans = sol.topKFrequent(nums, k)
print(ans)