#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def dfs(node):
            
            if node is None:
                return
            
            nonlocal sum

            if node.left is not None and node.left.left is None and node.left.right is None:                
                sum = sum + node.left.val
                        
            dfs(node.left)
            dfs(node.right)
            

        dfs(root)
        return sum
        
# @lc code=end

root = [3,9,20,None,None,15,7]
tree = arrayToTree(root)
sol = Solution()
ans = sol.sumOfLeftLeaves(tree)
print(ans)

