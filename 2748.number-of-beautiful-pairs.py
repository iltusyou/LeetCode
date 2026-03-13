#
# @lc app=leetcode id=2748 lang=python3
#
# [2748] Number of Beautiful Pairs
#

# @lc code=start
from math import gcd
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def get_first_last(x:int)->tuple:
            s = str(x)
            return (int(s[0]), x%10)

        pairs = list(map(get_first_last, nums))

        ans = 0

        n = len(nums)
        for i in range(0, n-1):
            for j in range(i+1, n):                
                if gcd(pairs[i][0], pairs[j][1]) == 1:
                    ans+=1            

        return ans



# @lc code=end

nums = [2,5,1,4]
# nums = [11,21,12]

sol = Solution()
ans = sol.countBeautifulPairs(nums)
print(ans)