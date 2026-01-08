from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0

        sortedG = sorted(g)
        sortedS = sorted(s)

        sIndex = len(sortedS) - 1
        gIndex = len(sortedG) - 1

        while sIndex > -1 and gIndex >-1:         
            canSatisfy = sortedS[sIndex] >= sortedG[gIndex]

            if canSatisfy:
                res += 1
                sIndex -= 1

            gIndex -= 1
    
        print(gIndex, sIndex)
        return len(s) - sIndex -1
    
# g = [1,2,3], s = [1,1]

sol = Solution()
ans = sol.findContentChildren(g = [1,2,3], s = [1,1])
print(ans)