#
# @lc app=leetcode id=3170 lang=python3
#
# [3170] Lexicographically Minimum String After Removing Stars
#

# @lc code=start
class Solution:
    def clearStars(self, s: str) -> str:
        stacks = [[] for i in range(26)]

        ans = [c for c in s]        

        for i, c in enumerate(s):          
            if c == '*':
                j = 0
                while len(stacks[j]) == 0:
                    j+=1
                                
                ans[stacks[j].pop()] = ''
                ans[i] = ''
                
            else:
                stacks[ord(c)-ord('a')].append(i)
                            
        return ''.join(ans) 
        
# @lc code=end

s = "aaba*"

sol = Solution()
ans = sol.clearStars(s)
print(ans)

