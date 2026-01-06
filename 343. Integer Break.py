class Solution:
    def integerBreak(self, n: int) -> int:        
        dp = [1] * (n+1)        
        for i in range(2, n+1):
            for j in range(1,(i//2)+1):                                

                dp[i] = max(dp[i], max((i-j)*j, dp[i-j]*j)) 
                print(i,j)
                 
        return dp[-1]
    

n = 10
sol = Solution()
ans = sol.integerBreak(n)
print(ans)