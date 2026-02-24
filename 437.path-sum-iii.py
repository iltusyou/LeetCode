#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, prefix_sum, d, res):
            if node is None:
                return 
                                    
            prefix_sum += node.val
            if prefix_sum - targetSum in d:
                res[0] += d[prefix_sum - targetSum]

            d[prefix_sum] = d.get(prefix_sum, 0) + 1            
            
            print(node.val, d, res[0])

            dfs(node.left, prefix_sum, d, res)
            dfs(node.right, prefix_sum, d, res)
            d[prefix_sum] -= 1

        
        res = [0]
        d={
            0:1
        }
        dfs(root, 0, d, res)
        return res[0]

# @lc code=end

# root = [10,5,-3,3,2,None,11,3,-2,None,1]
# targetSum = 8

root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22

tree = arrayToTree(root)
printTree(tree)

sol = Solution()
ans = sol.pathSum(tree, targetSum)
print(ans)


