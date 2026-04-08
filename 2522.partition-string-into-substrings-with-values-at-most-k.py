#
# @lc app=leetcode id=2522 lang=python3
#
# [2522] Partition String Into Substrings With Values at Most K
#

# @lc code=start
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:        
        tot, ans = 0, 1
        for c in s:
            cur = int(c)
            if cur > k and cur < 10:
                return -1

            tot = tot * 10 + cur
            if tot > k:
                tot = cur
                ans += 1
     
        return ans
        

        
        
# @lc code=end

s = "165462"
k = 60

# s = "238182"
# k = 5

sol = Solution()
ans = sol.minimumPartition(s,k)
print(ans)