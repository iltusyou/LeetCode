#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:                
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

        def printQ(i):
            return '.' * i + 'Q' + '.' * (n-1-i)

        def setQ(row, col, path):  
            if not check(row, col):
                return            
            
            record[row][col] = 1
            r[col] = 1

            path.append(dic[col])

            if row == n-1:                
                ans.append(path.copy())
                path.pop()
                record[row][col] = 0
                r[col] = 0
                return 

            for i in range(n):
                if i not in [col-1, col, col+1] and r[i] == 0:                                
                    setQ(row+1, i, path)

            path.pop()
            record[row][col] = 0
            r[col] = 0


        dic = {}
        for i in range(n):
            dic[i] = printQ(i)

        ans = []

        for i in range(n):
            setQ(0, i, [])
                    
        return ans
# @lc code=end

# n = 4
n = 5
sol = Solution()
ans = sol.solveNQueens(n)
print(ans)



# print(printQ(2, 8))