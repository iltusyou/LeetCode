#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel = 0        

        for i, e in  enumerate(s):
            

            if e in 'aeiou':
                vowel += 1
           
            ans = max(ans, vowel)
            
            left = i - k + 1
            print(i, e, vowel, left)

            if left < 0:
                continue


            if s[left] in 'aeiou':
                vowel -= 1

   
        return ans
        
# @lc code=end

# s = "abciiidef"
# k = 3

# s = "a"
# k = 1

s = "aeiou"
k = 2

sol = Solution()
ans = sol.maxVowels(s, k)
print(ans)