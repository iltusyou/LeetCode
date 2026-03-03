#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
from typing import List
import heapq


class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):        
        heapq.heapify(nums)                
        self.nums = nums
        print(self.nums)

    def add(self, val: int) -> int:        
        heapq.heappush(self.nums, val)

        while len(self.nums) > k:
            heapq.heappop(self.nums)
                        
        return self.nums[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

inputs2 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# inputs2 = [[1,[]],[-3],[-2],[-4],[0],[4]]
# inputs2 = [[2,[0]],[-1],[1],[-2],[-4],[3]]
# inputs2 = [[3,[5,-1]],[2],[1],[-1],[3],[4]]

k, nums = inputs2[0]
obj = KthLargest(k, nums)
for i in range(1, len(inputs2)):
    val = inputs2[i][0]
    param_1 = obj.add(val)
    print(param_1)
