#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#

# @lc code=start
class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = [1] * 5

        for _ in range(n-1):
            u = vowels[4]
            o = u + vowels[3]
            i = o + vowels[2]
            e = i + vowels[1]
            a = e + vowels[0]

            vowels = [a, e, i, o, u]

        return sum(vowels)
        
# @lc code=end

# n = 1
# n = 2
n= 33
n = 50

sol = Solution()
ans = sol.countVowelStrings(n)
print(ans)