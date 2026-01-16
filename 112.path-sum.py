#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False        
        
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

        def traversal(node, sum):                                    
            sum += node.val                    

            if not node.left and not node.right:                                
                return sum == targetSum
            
            return traversal(node.left, sum) or traversal(node.right, sum)
                                     
        return traversal(root, 0)
    
# @lc code=end

root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22

# root = [1,2,3]
# targetSum = 5

# root = []
# targetSum = 0

# root = [1,2]
# targetSum = 0

# tree = arrayToTree(root)
# sol = Solution()
# ans = sol.hasPathSum(tree, targetSum)
# print(ans)

print(None)