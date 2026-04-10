#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        def dfs(node, res, depth):
            if node is None:
                return -1
                        
            depth += 1
            l = dfs(node.left, res, depth) 
            r = dfs(node.right, res, depth)            
            d = max(l, r) + 1
            
            if l == r:
                cur = node, d, depth + d
                res.append(cur)
                
            # print(node.val, d, l, r, l == r, depth)

            return d
        
        res = []
        dfs(root, res, 0)
                        
        max_depth = max(depth for _,_,depth in res)


        res = [x for x in res if x[2] == max_depth]        


        max_d = max(d for _,d,_ in res)
        res = [x for x in res if x[1] == max_d]
        ans = res[0][0]

        return ans
# @lc code=end

null = None
root = [3,5,1,6,2,0,8,null,null,7,4]
# root = [3,5,1,6,2,0,8]

# root = [1]
# root = [0,1,3,null,2]
# root =[1,2,null,3,4,null,null,5]

tree = arrayToTree(root)

sol = Solution()
ans = sol.lcaDeepestLeaves(tree)
print(ans)