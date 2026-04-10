#
# @lc app=leetcode id=3080 lang=python3
#
# [3080] Mark Elements on Array by Performing Queries
#

# @lc code=start
from typing import List


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:        
        sorted_nums = sorted([(x, i) for i, x in enumerate(nums)]) 
        n, tot = len(nums), sum(nums)

        print(sorted_nums, n , tot)

        mark_index = 0

        ans = []
        for i, k in queries:
            s = nums[i]

            nums[i] = 0

            j = 0
            while j < k and mark_index < n:
                before_idx = sorted_nums[mark_index][1]
                mark_index += 1
                
                if nums[before_idx] == 0:                    
                    continue

                s += nums[before_idx]
                nums[before_idx] = 0                
                j += 1

            tot -= s
            ans.append(tot)

        return ans
    
# @lc code=end

nums = [1,2,2,1,2,3,1]
queries = [[1,2],[3,3],[4,2]]

sol = Solution()
ans = sol.unmarkedSumArray(nums, queries)
print(ans)