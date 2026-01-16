#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from utils import TreeNode, arrayToTree


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def traversal(node):
            if node is None:
                return []            
            return traversal(node.left) + [node.val] +  traversal(node.right)

        arr = traversal(root)

        minAbs = float('inf')
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < minAbs:
                minAbs = diff

        return minAbs
# @lc code=end



root = [1,0,48,None,None,12,49]
tree = arrayToTree(root)

sol = Solution()
ans = sol.getMinimumDifference(tree)
print(ans)