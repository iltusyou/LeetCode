#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        print(root)

        if root is None:
            return None

        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        
        if root.val < val:
            return self.searchBST(root.right, val)

        return
# @lc code=end

root = [4,2,7,1,3]
val = 2

# root = [4,2,7,1,3]
# val = 5

tree = arrayToTree(root)

sol = Solution()
ans = sol.searchBST(tree,val)
arr = treeToArray(ans)
print(arr)
