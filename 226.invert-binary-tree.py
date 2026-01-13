#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from utils import TreeNode, arrayToTree, printTree, treeToArray


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left) 
        self.invertTree(root.right) 

        return root
# @lc code=end


# root = [2,1,3]
root = [4,2,7,1,3,6,9]
tree = arrayToTree(root)

sol = Solution()
ans = sol.invertTree(tree)

arr = treeToArray(ans)
print(arr)