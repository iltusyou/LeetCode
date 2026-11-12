#
# @lc app=leetcode id=2747 lang=python3
#
# [2747] Count Zero Request Servers
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        queries = sorted([(x, i) for i, x in enumerate(queries)])
        logs = sorted(logs, key=lambda x: x[1])        
                        
        receive = [0] * (n+1)

        ans = [0] * len(queries)

        left, right = 0, 0
        cnt = 0

        for q, i in queries:                        
            while right < len(logs) and logs[right][1] <= q:                
                server_id, time = logs[right]

                if receive[server_id] == 0:
                    cnt += 1

                receive[server_id] += 1
                right += 1
                                          
            while left < len(logs) and logs[left][1] < q - x:
                server_id, time = logs[left]
                receive[server_id] -= 1

                if receive[server_id] == 0:
                    cnt -= 1

                left += 1
            
            ans[i] = n - cnt
            
            print(q, q-x, left, right, receive, ans)

        return ans
# @lc code=end

n = 3
logs = [[1,3],[2,6],[1,5]]
x = 5
queries = [10,11]

sol = Solution()
ans = sol.countServers(n, logs, x, queries)
print(ans)
