#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from collections import deque

class MyStack:

    def __init__(self):
        self.que = deque()
        
    def push(self, x: int) -> None:
        self.que.append(x)
        return

    def pop(self) -> int:        
        for i in range(0, len(self.que)-1):
            self.que.append(self.que.popleft())

        tmp = self.que.popleft()        
        return tmp

    def top(self) -> int:
        for i in range(0, len(self.que)-1):
            self.que.append(self.que.popleft())

        tmp = self.que.popleft()
        self.que.append(tmp)

        return tmp

    def empty(self) -> bool:        
        return len(self.que) == 0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
print(param_2)

param_3 = obj.top()
print(param_3)

param_4 = obj.empty()
print(param_4)
# @lc code=end

