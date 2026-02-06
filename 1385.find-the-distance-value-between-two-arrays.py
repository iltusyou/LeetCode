#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#

# @lc code=start
from typing import List


class Solution:                                    
    def findInsert(self, arr: List[int], target: int, d:int):      
        n = len(arr)

        if arr[0] > target:
            return target+d < arr[0]
        
        if arr[n-1] < target:
            return target-d > arr[n-1]
        
        left, right = 0, len(arr)-1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return False
            
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1              
                    
        return target-d > arr[left-1]  and target+d < arr[left]

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()

        count = 0
        for n in arr1:                       
            if self.findInsert(arr2, n, d):
                count += 1

        return count

        
# @lc code=end

# arr1 = [4,5,8]
# arr2 = [10,9,1,8]
# d = 2

# arr1 = [1,4,2,3]
# arr2 = [-4,-3,6,10,20,30]
# d = 3

# arr1 = [2,1,100,3]
# arr2 = [-5,-2,10,-3,7]
# d = 6

arr1 = [-3,-3,4,-1,-10]
arr2 = [7,10]
d = 12

sol = Solution()
ans = sol.findTheDistanceValue(arr1, arr2, d)
print(ans)


