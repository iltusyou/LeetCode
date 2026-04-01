#
# @lc app=leetcode id=2171 lang=python3
#
# [2171] Removing Minimum Number of Magic Beans
#

# @lc code=start
from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort(reverse= True)

        n = len(beans)
        remove = [0] * n
        remaining = beans[0]
        
        for i in range(1, n):            
            remove[i] = remove[i-1] + (remaining - beans[i]) * i
            remaining = beans[i]
            
        s = 0
        for i in range(n-1, -1, -1):                        
            remove[i] += s
            s += beans[i]
        
        ans = min(remove)                                          

        return ans
# @lc code=end

# beans = [4,1,6,5]
# beans = [2,10,3,2]
# beans = [66,90,47,25,92,90,76,85,22,3]
beans = [25,27,1,10,8,35,17,5,4,16]

sol = Solution()
ans = sol.minimumRemoval(beans)
print(ans)