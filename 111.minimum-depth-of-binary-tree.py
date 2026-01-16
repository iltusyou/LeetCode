#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if root.left is None and root.right is None:
                return 1

        def dfs(node):
            if node.left is None and node.right is None:
                return 1
             
            nodes = []                 
            
            if node.left is not None:
                nodes.append(dfs(node.left))
            
            if node.right is not None:
                nodes.append(dfs(node.right))
                                    
            return min(nodes) + 1

        res = dfs(root)

        return res 
        
# @lc code=end

# root = [3,9,20,None,None,15,7]
# root = [2,None,3,None,4,None,5,None,6]
# root = [2,3,4]
root = [2]

tree = arrayToTree(root)

sol = Solution()
ans = sol.minDepth(tree)
print(ans)