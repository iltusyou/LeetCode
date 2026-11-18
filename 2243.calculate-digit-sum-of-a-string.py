#
# @lc app=leetcode id=2243 lang=python3
#
# [2243] Calculate Digit Sum of a String
#

# @lc code=start
class Solution:    
    def digitSum(self, s: str, k: int) -> str:           
        n = len(s)

        if n <= k:
            return s

        new_s = ''

        for i in range(n//k):
            curr = sum(int(d) for d in s[i*k:i*k+k])
            new_s += str(curr)            

        if s[(i+1)*k:n]:
            curr = sum(int(d) for d in s[(i+1)*k:n])
            new_s += str(curr)

        return self.digitSum(new_s, k)
                
                

            

        
# @lc code=end

# s = "11111222223"
# k = 3

s = "1234"
k =2

sol = Solution()
ans = sol.digitSum(s, k)
print(ans)