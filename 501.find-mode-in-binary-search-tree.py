#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(node):
            if node is None:
                return []
            return traversal(node.left) + [node.val] + traversal(node.right)
        
        arr = traversal(root)

        curVal = arr[0]
        count = 0
        maxCount = 0
        res = []

        for i in range(len(arr)):
            if arr[i] != curVal:
                curVal = arr[i]
                count = 0

            count += 1
            if count > maxCount:
                maxCount = count
                res = [arr[i]]                

            elif count == maxCount:
                res.append(arr[i])

        return res
# @lc code=end

# root = [1,None,2,2]
# root = [0]
root = [1,None,2]

tree = arrayToTree(root)

sol = Solution()
ans = sol.findMode(tree)
print(ans)