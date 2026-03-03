#
# @lc app=leetcode id=2558 lang=python3
#
# [2558] Take Gifts From the Richest Pile
#

# @lc code=start
import bisect
from typing import List
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts.sort()
        
        while k and gifts[-1] > 1:
            n = math.isqrt(gifts.pop())
            i = bisect.bisect_left(gifts, n)
            gifts.insert(i, n)
                        
            k-=1
                                    
        return sum(gifts)
# @lc code=end

gifts = [25,64,9,4,100]
k = 4

sol = Solution()
ans = sol.pickGifts(gifts, k)
print(ans)





