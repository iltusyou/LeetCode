#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        arr = []
        arr.append(nums[0])

        for i in range(1, len(nums)):
            s = nums[i] + arr[-1]
            arr.append(s)

        print(arr)

        self.arr = arr                

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.arr[right]
        return self.arr[right] - self.arr[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)

testCase = [[0, 2], [2, 5], [0, 5]]
for t in testCase:
    left = t[0]
    right = t[1]
    param_1 = obj.sumRange(left,right)
    print(param_1)

