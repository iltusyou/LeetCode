#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:           
            return None

        maxVal = max(nums)
        idx = nums.index(maxVal)

        leftNums = nums[0:idx]
        rightNums = nums[idx+1: len(nums)]

        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(leftNums)
        root.right = self.constructMaximumBinaryTree(rightNums)

        return root


        
# @lc code=end

nums = [3,2,1,6,0,5]
sol = Solution()
ans = sol.constructMaximumBinaryTree(nums)
arr = treeToArray(ans)
print(arr)