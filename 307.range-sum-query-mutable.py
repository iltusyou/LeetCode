#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
from typing import List


class NumArray:
    __slots__ = 'nums', 'tree'

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = [0] * n
        self.tree = [0] * (n+1)

    def update(self, index: int, val: int) -> None:        
        delta = val - self.nums[index]
        self.nums[index] = val

        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            

        return

    def sumRange(self, left: int, right: int) -> int:
        return
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

for i in range(16):
    print(i, i+(i&-i))