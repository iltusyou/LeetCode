#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
from collections import defaultdict
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        dic = defaultdict(list)
        for i, x in enumerate(nums):
            dic[x].append(i)        

        self.dic = dic

    def pick(self, target: int) -> int:
        arr = self.dic[target]
        n = len(arr)
        if n == 1:
            return arr[0]

        random_index = random.randint(0, n-1)

        return arr[random_index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

inputs1 = ["Solution", "pick", "pick", "pick"]
inputs2 = [[[1, 2, 3, 3, 3]], [3], [1], [3]]

nums = inputs2[0][0]
obj = Solution(nums)

for op, val in zip(inputs1, inputs2):
    if op == "pick":
        target = val[0]
        param_1 = obj.pick(target)
        print(param_1)