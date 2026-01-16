#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional
from utils import TreeNode, arrayToTree

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:        
        
        queue = deque()
        queue.append(root)
        
        res = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    res = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return res
# @lc code=end

# root = [1,2,3,4,None,5,6,None,None,7]
# root = [2,1,3]
root = [1]

tree = arrayToTree(root)
sol = Solution()
ans = sol.findBottomLeftValue(tree)
print(ans)