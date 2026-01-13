#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
from utils import TreeNode, arrayToTree

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
# @lc code=end

# root = [1,None,2,3]
root = [1,2,3,4,5,None,8,None,None,6,7,9]

tree = arrayToTree(root)

sol = Solution()
ans = sol.postorderTraversal(tree)
print(ans)