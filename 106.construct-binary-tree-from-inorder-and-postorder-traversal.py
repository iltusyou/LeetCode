#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from utils import TreeNode, treeToArray

class Solution:
    def generateTree(self, inorder: List[int], postorder: List[int]):


            root = TreeNode(postorder[-1])
            print(root)

            idx = inorder.index(postorder[-1])
            leftInorder = inorder[0:idx]
            rightInorder = inorder[idx+1: len(inorder)]

            leftLength = len(leftInorder)
            leftPostorder = postorder[0:leftLength]
            rightPostorder = postorder[leftLength: len(postorder)-1]

            root.left = self.buildTree(leftInorder, leftPostorder)
            root.right = self.buildTree(rightInorder, rightPostorder)

            return root

            

            
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
                
        root = TreeNode(postorder[-1])

        idx = inorder.index(postorder[-1])
        leftInorder = inorder[0:idx]
        rightInorder = inorder[idx+1: len(inorder)]

        leftLength = len(leftInorder)
        leftPostorder = postorder[0:leftLength]
        rightPostorder = postorder[leftLength: len(postorder)-1]

        # print(inorder, postorder, leftInorder, rightInorder, leftPostorder, rightPostorder)

        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)

        return root
    
# @lc code=end

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

sol = Solution()
ans = sol.buildTree(inorder, postorder)
tree = treeToArray(ans)
print(tree)

