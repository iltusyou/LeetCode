#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            
            leftDepth = dfs(node.left) 
            rightDepth = dfs(node.right)

            return max(leftDepth, rightDepth) + 1
        
        res = dfs(root)

        return res 
        
# @lc code=end

root = [3,9,20,None,None,15,7]
tree = arrayToTree(root)

sol = Solution()
ans = sol.maxDepth(tree)
print(ans)


