#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



from typing import Optional

from utils import TreeNode, arrayToTree, treeToArray


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        
        if root1 is None and root2 is not None:
            # root2.left = self.mergeTrees(None, root2.left)
            # root2.right = self.mergeTrees(None, root2.right)
            return root2
        
        if root2 is None and root1 is not None:
            # root1.left = self.mergeTrees(root1.left, None)
            # root1.right = self.mergeTrees(root1.right, None)
            return root1
        

        root1.val += root2.val        
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1

        
# @lc code=end

root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]

tree1 = arrayToTree(root1)
tree2 = arrayToTree(root2)

sol = Solution()
ans = sol.mergeTrees(tree1, tree2)
arr = treeToArray(ans)
print(arr)