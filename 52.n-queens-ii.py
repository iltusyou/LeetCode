#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        r = [0 for _ in range(n)] #直是否重複

        record = [[0 for _ in range(n)] for _ in range(n)]     
        
        def check(row, col):                        
            for i in range(row):                
                up = row - (i+1)

                left = col-i-1                
                if left >= 0 and record[up][left] == 1:
                    return False

                right = col+i+1                
                if right <= n-1 and record[up][right] == 1:
                    return False

            return True

        def setQ(row, col):  
            if not check(row, col):
                return            
            
            record[row][col] = 1
            r[col] = 1

            if row == n-1:                
                ans[0] += 1

                record[row][col] = 0
                r[col] = 0
                return 

            for i in range(n):
                if i not in [col-1, col, col+1] and r[i] == 0:                                
                    setQ(row+1, i)

            record[row][col] = 0
            r[col] = 0

        ans = [0]

        for i in range(n):
            setQ(0, i)
                    
        return ans[0]
# @lc code=end

n = 4

sol = Solution()
ans = sol.totalNQueens(n)
print(ans)