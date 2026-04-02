#
# @lc app=leetcode id=3319 lang=python3
#
# [3319] K-th Largest Perfect Subtree Size in Binary Tree
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
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, arr):
            if node is None:
                cur = 0

            else:
                left = dfs(node.left, arr)
                right = dfs(node.right, arr)

                if left == right and left >= 0 and right >= 0:
                    cur = left * 2 + 1
                else:
                    cur = -1
            
            if cur > 0:            
                arr.append(cur)
            return cur
                                    
        arr = []
        dfs(root, arr)        
        print(arr)

        arr.sort(reverse = True)        
        ans = -1 if k-1 >= len(arr) else arr[k-1]
        return ans
    
# @lc code=end

null = None

# root = [5,3,6,5,2,5,7,1,8,null,null,6,8]
# k = 2

root = [1,2,3,null,4]
k = 3

# root = [1]
# k = 1

tree = arrayToTree(root)

sol = Solution()
ans = sol.kthLargestPerfectSubtree(tree, k)
print(ans)