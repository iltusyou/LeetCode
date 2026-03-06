#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:

        if len(self.left) == len(self.right):
            heapq.heappush_max(self.left, heapq.heappushpop(self.right, num))        
        else:
            heapq.heappush(self.right, heapq.heappushpop_max(self.left, num))                            
    
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0]

        return (self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

inputs1 = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
inputs2 = [[], [1], [2], [], [3], []]

obj = MedianFinder()
for op, num in zip(inputs1, inputs2):
    if op == 'addNum':
        obj.addNum(num[0])
        continue

    if op == 'findMedian':
        param_2 = obj.findMedian()
        print(param_2)
        continue


a = heapq.heappushpop([], 1)
print(a)