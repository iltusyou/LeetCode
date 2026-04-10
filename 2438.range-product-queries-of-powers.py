#
# @lc app=leetcode id=2438 lang=python3
#
# [2438] Range Product Queries of Powers
#

# @lc code=start
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = []
        s, i = 0, 1
        while s < 10 ** 9:
            arr.append(i)
            s += i
            i *= 2

        arr = sorted(arr, reverse = True)     

        arr2, i = [], 0
        while n > 0:
            if n >= arr[i]:
                arr2.append(arr[i])
                n -= arr[i]
            i+=1

        arr2 = sorted(arr2)             
        power = [arr2[0]]
        

        for i in range(1, len(arr2)):
            p = power[i-1] * arr2[i]
            power.append(p)

        ans = []
        MOD = 1000000007
        for left, right in queries:
            if left == 0:
                a = power[right]
            else:
                a = power[right] // power[left-1]
            a = a % MOD
            ans.append(a)
            
        return ans
        
# @lc code=end

n = 15
queries = [[0,1],[2,2],[0,3]]

sol = Solution()
ans = sol.productQueries(n, queries)
print(ans)
