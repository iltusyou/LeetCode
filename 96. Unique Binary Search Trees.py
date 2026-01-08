class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            t = i//2
            for j in range(0, t):
                dp[i] = dp[i] + (dp[j]*dp[i-1-j])*2

            if i%2==1:
                dp[i] = dp[i] + (dp[t]*dp[t])


        # dp[2] = dp[2] + dp[0]*dp[1]
        # dp[2] = dp[2] + dp[1]*dp[0]

        # dp[3] = dp[3] + dp[0]*dp[2]
        # dp[3] = dp[3] + dp[1]*dp[1]
        # dp[3] = dp[3] + dp[2]*dp[0]        

        # dp[4] = dp[4] + dp[0]*dp[3]
        # dp[4] = dp[4] + dp[1]*dp[2]
        # dp[4] = dp[4] + dp[2]*dp[1]
        # dp[4] = dp[4] + dp[3]*dp[0]

        return dp[n]


        
    
n = 4
sol = Solution()
ans = sol.numTrees(n)
print(ans)