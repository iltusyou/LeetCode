#
# @lc app=leetcode id=2684 lang=python3
#
# [2684] Maximum Number of Moves in a Grid
#

# @lc code=start
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid.append([1000001] * n)                

        idx = [[1 for _ in range(n)] for _ in range(m)]

        for col in range(1, n):         
            for row in range(m):
                curr = grid[row][col]                      
              
                if row > 0 and idx[row-1][col-1] == 1 and curr > grid[row-1][col-1]:
                    idx[row][col] = 1
          
                elif idx[row][col-1] == 1 and curr > grid[row][col-1]:
                    idx[row][col] = 1
                  
                elif row < m-1 and idx[row+1][col-1] == 1 and curr > grid[row+1][col-1]:
                    idx[row][col] = 1
                
                else:
                    idx[row][col] = 0
                            
            col_sum = sum(idx[r][col] for r in range(m)) 
            if col_sum == 0:
                return col - 1
            
        return n-1
      
        
# @lc code=end

# grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# grid = [[3,2,4],[2,1,9],[1,1,7]]
grid = [[1000000,92910,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068],[1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118]]
# grid = [[187,167,209,251,152,236,263,128,135],[267,249,251,285,73,204,70,207,74],[189,159,235,66,84,89,153,111,189],[120,81,210,7,2,231,92,128,218],[193,131,244,293,284,175,226,205,245]]

sol = Solution()
ans = sol.maxMoves(grid)
print(ans)