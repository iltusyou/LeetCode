#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.queue = []
        return

    def push(self, x: int) -> None:
        self.queue.append(x)
        return

    def pop(self) -> int:
        res = None
        if not self.empty():
            res = self.peek()
            self.queue.pop(0)
        return res

    def peek(self) -> int:        
        if self.empty():
            return None
        return self.queue[0]

    def empty(self) -> bool:        
        return True if len(self.queue) == 0 else False 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

