#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from utils import TreeNode, arrayToTree, printTree


class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):                        

            if node.left is None and node.right is None:                
                return (node.val, node.val, True)
            
            maxVal = node.val
            minVal = node.val
            isValid = True            

            if node.left is not None:
                leftMin, leftMax, leftValid = traverse(node.left)                             
                isValid = (node.val>leftMax) and leftValid
                minVal = leftMin                
                
            if node.right is not None:
                rightMin, rightMax, rightValid = traverse(node.right)             
                isValid = isValid and (node.val<rightMin) and rightValid                        
                maxVal = rightMax                
                            
            return (minVal, maxVal, isValid)
                            
        res = traverse(root)
        return res[2]
        
# @lc code=end

# root = [5,1,4,None,None,3,6]
# root = [1]
root = [32,26,47,19,None,None,56,None,27]
tree = arrayToTree(root)
# printTree(tree)


sol = Solution()
ans = sol.isValidBST(tree)
print(ans)

