#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        res = [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        print(root.val, res)        
        return res
    

# @lc code=end

# nums = [1,None,2,3]
nums = [1,2,3,4,5,None,8,None,None,6,7,9]
root = arrayToTree(nums)

sol = Solution()
ans = sol.preorderTraversal(root)
print(ans)

