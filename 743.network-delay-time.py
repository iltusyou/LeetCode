#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict, deque
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
         
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        graph = [[] for _ in range(n+1)]
        for t in times:
            u, v, w = t
            graph[u].append((v, w))        
                
        heap = [(0, k)]
        heapq.heapify(heap)        
        
        while heap:
            time, node = heapq.heappop(heap)        

            if time > dist[node] :
                continue
                        
            for v, w in graph[node]:
                accu_time = time + w

                if accu_time < dist[v]:
                    dist[v] = accu_time
                    heapq.heappush(heap, (accu_time, v))
       
        
        ans = max(dist[1:])
        return -1 if ans == float('inf') else ans
    
# @lc code=end

# times = [[2,1,1],[2,3,1],[3,4,1]]
# n = 4
# k = 2

# times = [[1,2,1]]
# n = 2
# k = 2

# times = [[1,2,1],[2,1,3]]
# n = 2
# k = 2

times = [[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]]
n = 5
k = 3

sol = Solution()
ans = sol.networkDelayTime(times, n, k)
print(ans)