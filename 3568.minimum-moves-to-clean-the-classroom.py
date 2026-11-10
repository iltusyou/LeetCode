#
# @lc app=leetcode id=3568 lang=python3
#
# [3568] Minimum Moves to Clean the Classroom
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        ldic = {}
        litter = 0
        start = None
        mask, move = 0, 0

        for i, row in enumerate(classroom):
            for j, x in enumerate(row):
                if x == 'L':
                    ldic[(i,j)] = litter
                    litter += 1

                if x == 'S':
                    start = (i, j, mask, energy, move)
                
        que = deque()
        que.append(start)

        visited = defaultdict(list)
        
        while que:
            
            row, col, mask, e, move = que.popleft()            

            # print(row, col, mask, e, move, classroom[row][col], que)            

            match classroom[row][col]:
                case 'L':
                    mask |= 1 << ldic[(row, col)]
                case 'R':
                    e = energy

            if mask == (1 << litter) - 1:                            
                    return move
                        
            if e == 0 :
                continue

            state = (row, col, mask)

            if any(e <= old_e and move >= old_m for old_e, old_m in visited[state]) :
                continue

            visited[state] = [ (old_e, old_m) for old_e, old_m in visited[state] if old_e > e or old_m < move]
            visited[state].append((e, move))

            if col < n-1 and classroom[row][col+1] != 'X':       
                que.append((row, col + 1, mask, e-1, move+1))
                                        
            if col > 0 and classroom[row][col-1] != 'X':          
                que.append((row, col-1, mask, e-1, move+1))
                                        
            if row < m-1 and classroom[row+1][col] != 'X':       
                que.append((row+1, col, mask, e-1, move+1))                            
            
            if row > 0 and classroom[row-1][col] != 'X':   
                que.append((row-1, col, mask, e-1, move+1))
                                  
        return -1
        
# @lc code=end

# classroom = ["S.", "XL"]
# energy = 2

classroom = ["L.S", "RXL"]
energy = 3

# classroom = ["L.S", "..R", "L.X", "XLR", "..L"]
# energy = 8

# classroom = ["RRL.", "LSXX", "RL.L", "LLL.", "L..."]
# energy = 15

# classroom = ["L.R.X", ".RLXR", ".RRLX", "L.XXX", "LSR.R", "L.RRX"]
# energy = 9

sol = Solution()
ans = sol.minMoves(classroom, energy)
print(ans)

