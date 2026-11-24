#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        dic = defaultdict(list)
        ans = [1] * n

        def backtracking(idx):            
            if dic[s[idx]]:
                parent[idx] = dic[s[idx]][-1]                
                            
            dic[s[idx]].append(idx)
            
            for i in children[idx]:
                backtracking(i)

            ans[parent[idx]] += ans[idx]
           
            dic[s[idx]].pop()
                    
        backtracking(0)        

        ans[-1] -= n

        return ans
# @lc code=end


parent = [-1,0,0,1,1,1]
s = "abaabc"

sol = Solution()
ans = sol.findSubtreeSizes(parent, s)
print(ans)
