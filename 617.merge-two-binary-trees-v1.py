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
from collections import deque
from typing import Optional

from utils import TreeNode, arrayToTree, treeToArray


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:            
            return None

        if root1 is None or root2 is None:
            val1 = 0 if root1 is None else root1.val
            val2 = 0 if root2 is None else root2.val
            return TreeNode(val1 + val2)


        que1 =  deque([root1])
        que2 =  deque([root2])        

        root = TreeNode(root1.val + root2.val)
        que = deque([root])

        while que1 and que2:
            node1 = que1.popleft()
            node2 = que2.popleft()
            node = que.popleft()

            if node1.left is not None or node2.left is not None:
                if node1.left is None:
                    node1.left = TreeNode(0)

                if node2.left is None:
                    node2.left = TreeNode(0)

                node.left = TreeNode(node1.left.val + node2.left.val)

                que1.append(node1.left)
                que2.append(node2.left)
                que.append(node.left)

            if node1.right is not None or node2.right is not None:
                if node1.right is None:
                    node1.right = TreeNode(0)

                if node2.right is None:
                    node2.right = TreeNode(0)

                node.right = TreeNode(node1.right.val + node2.right.val)

                que1.append(node1.right)
                que2.append(node2.right)
                que.append(node.right)                    

        return root
# @lc code=end

# root1 = [1,3,2,5]
# root2 = [2,1,3,None,4,None,7]

# root1 = []
# root2 = [1]

root1 = []
root2 = []

tree1 = arrayToTree(root1)
tree2 = arrayToTree(root2)

sol = Solution()
ans = sol.mergeTrees(tree1, tree2)
arr = treeToArray(ans)
print(arr)
