#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):            
            if not node:                
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            print(node.val, leftHeight, rightHeight)

            if leftHeight is False or rightHeight is False:
                return False
            
            if abs(leftHeight - rightHeight) > 1:
                return False

            height = max(leftHeight,rightHeight) + 1 
            
            return height
        
        res = dfs(root) is not False

        return res
# @lc code=end

# root = [3,9,20,None,None,15,7]
root = [1,2,2,3,3,None,None,4,4]
tree = arrayToTree(root)
sol = Solution()
ans = sol.isBalanced(tree)
print(ans)