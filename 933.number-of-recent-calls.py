#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
from collections import deque


class RecentCounter:

    def __init__(self):
        self.que = deque()

    def ping(self, t: int) -> int:
        self.que.append(t)
        while self.que[0] < t - 3000:
            self.que.popleft()

        return len(self.que)

       




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

obj = RecentCounter()

inputs = [[1], [100], [3001], [3002]]
for t in inputs:
    param_1 = obj.ping(t[0])
    print(param_1)