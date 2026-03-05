#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#

# @lc code=start
from typing import List

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d = {}
        for b in barcodes:
            d[b] = d.get(b, 0) + 1            
        
        t = sorted([[k, d[k]] for k in d.keys()], key= lambda x:x[1]) 
        print(d, t)

        # ans = []
        # while len(t) > 0:
        #     for k, v in t:
        #         print()


        

        return
# @lc code=end

barcodes = [1,1,1,1,2,2,3,3]
sol = Solution()
ans = sol.rearrangeBarcodes(barcodes)
print(ans)
