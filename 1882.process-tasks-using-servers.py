#
# @lc app=leetcode id=1882 lang=python3
#
# [1882] Process Tasks Using Servers
#

# @lc code=start
from collections import deque
import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        
        free = [(weight , index)for index, weight in enumerate(servers)]
        tasks = [(index, time) for index, time in enumerate(tasks)]
        tasks = deque(tasks)

        heapq.heapify(free)

        lock = []
        ans = []

        sec = 0
        while tasks:
            while lock and lock[0][0] == sec:
                _, l_w, l_i = heapq.heappop(lock)
                heapq.heappush(free, (l_w, l_i))

            while free and tasks and tasks[0][0] <= sec:
                t_i, t_t = tasks.popleft()
                f_w, f_i = heapq.heappop(free)
                heapq.heappush(lock, (sec + t_t, f_w, f_i))
                ans.append(f_i)

            if free:
                sec += 1
            else:
                sec = lock[0][0]
        
        return ans

        




        
# @lc code=end

servers = [3,3,2]
tasks = [1,2,3,2,1,2]

# servers = [10,63,95,16,85,57,83,95,6,29,71]
# tasks = [70,31,83,15,32,67,98,65,56,48,38,90,5]

sol = Solution()
ans = sol.assignTasks(servers, tasks)
print(ans)