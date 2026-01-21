#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
import re
from typing import List


class Solution:
    def isValidNumber(self, s):                
        if len(s) > 3:
            return False
        
        if s[0] == '0' and len(s) > 1:
            return False        
        
        num = int(s)
        return num >= 0 and num <= 255        

    def backTracking(self, s, startIndex, path, res):
        if len(path) == 4 and startIndex == len(s):            
            res.append('.'.join(path))
            return
         
        if startIndex >= len(s):
            return
               
        for i in range(startIndex, len(s)):                        
            if len(path) == 3 and (len(s) - i) > 3:
                # print('break', path, len(s) , i)
                break

            if len(path) > 4:
                break

            num = s[startIndex:i+1]

            if not self.isValidNumber(num):
                break

            # print(path, num, startIndex, i)

            path.append(num)
            self.backTracking(s, i+1, path, res)
            path.pop()  


    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.backTracking(s, 0, [], res)
        return res
    

        
# @lc code=end

s = "25525511135"
# s = "101023"

sol = Solution()
ans = sol.restoreIpAddresses(s)
print(ans)