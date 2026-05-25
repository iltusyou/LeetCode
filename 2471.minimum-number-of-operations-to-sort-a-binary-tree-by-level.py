#
# @lc app=leetcode id=2471 lang=python3
#
# [2471] Minimum Number of Operations to Sort a Binary Tree by Level
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

from utils import TreeNode, arrayToTree


class Solution:
    def swap(self, arr: list[int]) -> int:
        print(arr)
        n = len(arr)
        sorted_arr = sorted([(v, i) for i, v in enumerate(arr)])     
        sorted_arr = [i for _, i in sorted_arr]
        print(sorted_arr)

        ans = 0
        done = set()

        for i in range(n):
            if i == sorted_arr[i]: #不需更動
                done.add(i)
                continue

            curr, cnt = sorted_arr[i], 0
            while curr not in done:                
                done.add(curr)
                curr = sorted_arr[curr]
                cnt += 1

            if cnt > 0:                        
                ans += cnt- 1
          
        return ans


    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        que = [root]
        ans = 0

        while que:            
            cur_val = [q.val for q in que]                        
            que = [child for q in que for child in (q.left, q.right) if child is not None]
            cnt = self.swap(cur_val)
            ans += cnt
        
        return ans
# @lc code=end

null = None
root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
# root = [250,31,207,null,322,191,10,281,25,500,96,156,495,459,421,null,283,null,118,null,325,null,72,228,293,402,132,136,null,null,null,null,null,null,null,null,null,188,null,null,null,null,null,null,null,null,155,null,279,null,null,103,239,316,null,null,429,null,null,22,60,null,243,null,217]

tree = arrayToTree(root)
sol = Solution()
ans = sol.minimumOperations(tree)
print(ans)

# print(sol.swap([281, 25, 500, 96, 156, 495]))
