#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
                
        def dfs(node):
            if not node:
                return 0
            
            return 1 + dfs(node.left) + dfs(node.right)
            
        res = dfs(root)

        return res
# @lc code=end

root = [1,2,3,4,5,6]
tree = arrayToTree(root)
sol = Solution()
ans = sol.countNodes(tree)

print(ans)