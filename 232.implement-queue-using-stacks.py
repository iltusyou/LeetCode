#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []        

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        return

    def pop(self) -> int:
        if self.empty():
            return None
        
        self.move()        
        return self.stack_out.pop()

    def peek(self) -> int:        
        self.move()        
        return self.stack_out[-1]

    def empty(self) -> bool:        
        return not (self.stack_in or self.stack_out)
    
    def move(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

