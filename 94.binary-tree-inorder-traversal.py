#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
                
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
# @lc code=end

root = [1,2,3,4,5,None,8,None,None,6,7,9]
tree = arrayToTree(root)

sol = Solution()
ans = sol.inorderTraversal(tree)
print(ans)