#
# @lc app=leetcode id=3607 lang=python3
#
# [3607] Power Grid Maintenance
#

# @lc code=start
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        g = [[] for _ in range(c+1)]

        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        done = [-1] * (c+1) #判斷有無處理過

        def dfs(x: int, h):            
            done[x] = 0
            h.append(x) 

            for j in g[x]:                               
                if done[j] < 0:        
                    dfs(j, h)

        heap_dic = defaultdict(list)     
        for i in range(1, c+1):
            h = []            
            dfs(i, h)
            print(h)
            if len(h) > 1:
                heapq.heapify(h)
                for x in h:
                    heap_dic[x] = h


        ans = []
        offline = set()
        for op, sat in queries:
            if op == 1:
                if sat not in offline:
                    ans.append(sat)    
                    continue

                while heap_dic[sat] and heap_dic[sat][0] in offline:
                    heapq.heappop(heap_dic[sat])
                
                a = heap_dic[sat][0] if heap_dic[sat] else -1
                ans.append(a)
                continue

            if op == 2:
                offline.add(sat)

        return ans
        
        

    
            
                




        
        
# @lc code=end

# c = 5
# connections = [[1,2],[2,3],[4,5]]
# queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

c = 3
connections = []
queries = [[1,1],[2,1],[1,1]]

# c = 9
# connections = [[4,3],[4,9],[3,1],[9,2],[5,7],[9,8],[7,4],[6,2],[7,1],[4,8],[3,6],[5,3],[5,9],[8,2],[9,1],[8,5],[2,4],[2,1],[1,5],[6,1],[1,8],[6,4],[7,3],[7,9],[5,2],[9,6],[1,4],[2,3],[7,2],[7,8]]
# queries = [[1,8],[2,8],[2,6],[1,7],[1,7],[2,3],[2,1],[2,3],[2,5],[2,5],[2,6],[2,3],[1,2],[1,2],[1,4],[2,1],[1,2],[1,5],[2,2],[1,7],[2,9],[1,8],[2,1],[2,3],[2,5],[2,5],[2,6],[2,6],[1,7],[1,7],[2,4],[1,9],[1,3],[2,9],[1,8],[2,6],[2,8],[2,6],[1,7],[2,6]]

sol = Solution()
ans = sol.processQueries(c, connections, queries)
print(ans)