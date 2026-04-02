#
# @lc app=leetcode id=2447 lang=python3
#
# [2447] Number of Subarrays With GCD Equal to K
#

# @lc code=start
from math import gcd
from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:        
        n = len(nums)
        arr = [0] * n

        for i, x in enumerate(nums):
            if x % k == 0:
                arr[i] = x//k                

        print(arr)    
        ans = 0        
        for i, x in enumerate(arr):
            if x == 0:
                continue

            cur_gcd = x            
            if cur_gcd == 1:
                print('add x', x)
                ans += 1

            # 找開始互質到出現0的區間
            for j in range(i+1, n):
                if arr[j] == 0:
                    break
                
                if cur_gcd != 1:
                    cur_gcd = gcd(cur_gcd, arr[j])                

                if cur_gcd == 1:
                    print('add arr[j]', x, arr[j])
                    ans += 1                                

            if cur_gcd != 1:
                break

        return ans
# @lc code=end

# nums = [9,3,1,2,6,3]
# k = 3

# nums = [3,12,9,6]
# k = 3

nums = [3,3,4,1,2]
k = 1

sol = Solution()
ans = sol.subarrayGCD(nums, k)
print(ans)