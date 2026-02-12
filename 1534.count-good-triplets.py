#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#

# @lc code=start
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = len(arr)

        res = 0

        for j in range(1, l - 1):            
            for i in range(0, j):                
                for k in range(j+1, l):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        res += 1
            
        return res
    
# @lc code=end

# arr = [3,0,1,1,9,7]
# a = 7
# b = 2
# c = 3

arr = [1,18,19,2,19,10,2,5,15,18]
a = 4
b = 9
c = 2


sol = Solution()
ans = sol.countGoodTriplets(arr, a, b, c)
print(ans)

# newArr = sol.plusArr(arr, 1 ,2)
# print(newArr)
