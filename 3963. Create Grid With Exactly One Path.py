class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        l = '.' + '#' * (n-1)
        ans = [l for i in range(m-1)]
        ans.append('.'*n)
       
        return ans

m = 2
n = 3


sol = Solution()
ans = sol.createGrid(m, n)
print(ans)