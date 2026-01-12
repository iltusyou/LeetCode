#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        dic = {}
        lastIndex = [0] * n

        for i in range(n-1, -1, -1):
            if s[i] not in dic:
                dic[s[i]] = i

            lastIndex[i] = dic[s[i]]

        last = 0
        res = []

        for i in range(0, n):
            last = max(last, lastIndex[i])                

            if last == i:
                last = 0                
                res.append(i)

        for i in range(len(res)-1, 0, -1):
            res[i] = res[i] - res[i-1]
            
        res[0]+=1

        return res
# @lc code=end

s = "ababcbacadefegdehijhklij"
sol = Solution()
ans = sol.partitionLabels(s)
print(ans)