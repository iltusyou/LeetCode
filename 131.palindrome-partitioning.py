#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List


class Solution:
    def computePalindrome(self, s, isPalindrome):
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):              
                if i == j:
                    isPalindrome[i][j] = True                    
                elif j - i == 1:
                    isPalindrome[i][j] = (s[i] == s[j])
                else:
                    isPalindrome[i][j] = (s[i] == s[j]) and isPalindrome[i+1][j-1]


    def backTracking(self, startIndex, path, s, res, isPalindrome):
        if startIndex >= len(s):
                res.append(path[:])
                return        
                        
        for i in range(startIndex, len(s)):                            
            if isPalindrome[startIndex][i]:
                subStr = s[startIndex:i+1]
                path.append(subStr)                
                self.backTracking(i+1, path, s, res, isPalindrome)
                path.pop()
            
    def partition(self, s: str) -> List[List[str]]:
        res = []
        isPalindrome = [[False] *len(s) for _ in range(len(s))]
        self.computePalindrome(s, isPalindrome)    
        self.backTracking(0, [], s, res, isPalindrome) 
        
        return res
    
# @lc code=end


# s = "aab"
# s = "a"
s = "efe"

sol = Solution()
ans = sol.partition(s)
print(ans)