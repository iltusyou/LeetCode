#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        ans = []
        curr = 0

        for i in range(1, n+1):
            ans.append('Push')

            if i == target[curr]:
                curr += 1

                if curr == len(target):
                    return ans

            else:
                ans.append('Pop')

        
                                    
# @lc code=end

# target = [1,3]
# n = 3

# target = [1,2,3]
# n = 3

target = [1,2]
n = 4

sol = Solution()
ans = sol.buildArray(target, n)
print(ans)

