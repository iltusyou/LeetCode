#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        arr = [0] * (n + 1) 

        cnt = 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                cnt += 1
            arr[i] = cnt

        cnt = 0
        for i in range(n):
            if s[i] == '1':
                cnt += 1
            arr[i+1] = cnt + arr[i+1]

        ans = min(arr)

        return ans
# @lc code=end

# s = "00011000"
# s = "0101100011"
s = "10011111110010111011"
sol = Solution()
ans = sol.minFlipsMonoIncr(s)
print(ans)