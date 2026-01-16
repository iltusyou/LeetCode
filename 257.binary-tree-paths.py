#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):            

            if node.left is None and node.right is None:                
                res.append(path)
                return
            
            if node.left is not None:               
                p = path + f"->{node.left.val}"
                dfs(node.left, p)
            
            if node.right is not None:         
                p = path + f"->{node.right.val}"   
                dfs(node.right, p)
                                                
        dfs(root, f"{root.val}")

        return res
# @lc code=end

# root = [1,2,3,None,5]
root = [1]
tree = arrayToTree(root)
sol = Solution()
ans = sol.binaryTreePaths(tree)
print(ans)
