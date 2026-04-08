#
# @lc app=leetcode id=2546 lang=python3
#
# [2546] Apply Bitwise Operations to Make Strings Equal
#

# @lc code=start
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:

        s_cnt0, s_cnt1 = s.count('0'), s.count('1')        
        
        target_cnt0, target_cnt1 = target.count('0'), target.count('1')        

        if target_cnt0 == len(target) and s_cnt1 > 0:
            return False
        
        if s_cnt0 == len(s) and target_cnt1 > 0:
            return False
        
        print(s_cnt0, s_cnt1, target_cnt0, target_cnt1)
                
        return True

# @lc code=end

# s = "1010"
# target = "0110"

# s = "11"
# target = "00"

s = "00"
target = "10"

sol = Solution()
ans = sol.makeStringsEqual(s, target)
print(ans)