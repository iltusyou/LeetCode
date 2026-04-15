#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = []
        even_cnt = 0

        for n in nums:          
            if n % 2 == 1:
                arr.append(even_cnt)
                even_cnt = 0                                       
                arr.append('o')
                
            else:
                even_cnt += 1
                
        arr.append(even_cnt)
        
        print(arr)

        que, ans, odd = deque(), 0, 0
        for i, a in enumerate(arr):
            que.append(a)
           
            if a == 'o':
                odd += 1

            if odd == k:
                print(i, a, que, odd)
                ans += (que[0] + 1) * (arr[i+1] + 1)
                que.popleft()
                que.popleft()
                odd -= 1
                
        return ans
# @lc code=end

# nums = [1,1,2,1,1]
# k = 3

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

sol = Solution()
ans = sol.numberOfSubarrays(nums, k)
print(ans)