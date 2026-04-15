#
# @lc app=leetcode id=3132 lang=python3
#
# [3132] Find the Integer Added to Array II
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
       
        n = len(nums2)
        d = [0] * n
        nums1.sort()
        nums2.sort()
                
        for i in range(1, n):
            d[i] = nums2[i] - nums2[i-1]

        dic = defaultdict(int)
        for x in nums1:
            dic[x] += 1

        print(d, dic)        

        def isPossible(k, dic, d):
            s = k
            for i in d:
                s += i
                if dic[s] == 0:
                    return False
                dic[s] -= 1
            
            return True

        ans = float('inf')
        
        for k in nums1[0], nums1[1], nums1[2]:
            dic_copy = dic.copy()
            if isPossible(k, dic_copy, d):
                ans = min(ans, nums2[0] - k)

        return ans
                 
# @lc code=end

nums1 = [4,20,16,12,8]
nums2 = [14,18,10]

sol = Solution()
ans = sol.minimumAddedInteger(nums1, nums2)
print(ans)