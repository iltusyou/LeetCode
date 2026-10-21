#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
from typing import List


class NumArray:
    __slots__ = 'tree', 'n'
    
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree =  [0] * (4 * self.n)

        def build(node, start, end):
                        
            if start == end:
                self.tree[node] = nums[start]
                
            else:
                mid = (start + end) // 2
                left = build(node * 2,  start, mid)
                right = build(node * 2 +1,  mid + 1, end)
                self.tree[node] = left + right

            return self.tree[node]

        build(1, 0, self.n-1)

        print('init', self.tree)
            
                 
    def update(self, index: int, val: int) -> None:        
        self.updateTree(1, 0, self.n-1, index, val)                    

        return
    
    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeTree(1, 0, self.n - 1, left, right)                

    def updateTree(self, node, start, end, index, val):       
        
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2
        
        if index <= mid:
            self.updateTree(node * 2,  start, mid, index, val)
        else:
            self.updateTree(node * 2 +1,  mid+1, end, index, val)

        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

        return

    def sumRangeTree(self, node, start, end, left, right):

        # print(node, start, end, left, right)

        if end < left or right < start:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2

        return  self.sumRangeTree(node * 2, start, mid, left, right) + self.sumRangeTree(node * 2 + 1, mid + 1, end, left, right)

   

        


    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

# in1 = ["NumArray", "sumRange", "update", "sumRange"]
# in2 = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]

# in1 = ["NumArray","update","sumRange","sumRange","update","sumRange"]
# in2 = [[[9,-8]],[0,3],[1,1],[0,1],[1,-3],[0,1]]
#[null,null,-8,-5,null,0]

in1 = ["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
in2 = [[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]

obj = NumArray(in2[0][0])
ans = [None]

for i in range(1, len(in2)):
    op, parm = in1[i], in2[i]

    if op == 'update':
        idx, val = parm
        obj.update(idx, val)
        ans.append(None)

    if op == 'sumRange':
        left, right = parm
        res = obj.sumRange(left, right)
        print(res)
        ans.append(res)

print(ans)

    