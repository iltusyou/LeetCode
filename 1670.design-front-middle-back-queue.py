#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()

    def check(self):
        # 後面只能比前面多一個
        len1 = len(self.que1)
        len2 = len(self.que2)

        if len2 > len1 + 1:
            self.que1.append(self.que2.popleft())
        elif len1 > len2:
            self.que2.appendleft(self.que1.pop())

        print(self.que1, self.que2)

    def pushFront(self, val: int) -> None:
        self.que1.appendleft(val)
        self.check()
        
    def pushMiddle(self, val: int) -> None:
        self.que2.appendleft(val)
        self.check()
        
    def pushBack(self, val: int) -> None:
        self.que2.append(val)
        self.check()

    def popFront(self) -> int:
        if self.que1:
            res = self.que1.popleft()
        elif self.que2:
            res = self.que2.popleft()
        else:
            res = -1
        self.check()
        return res

    def popMiddle(self) -> int:
        if len(self.que2) > len(self.que1):
            res = self.que2.popleft()
        elif self.que1:
            res = self.que1.pop()
        else:
            res = -1

        self.check()
        return res                

    def popBack(self) -> int:
        if self.que2:
            res = self.que2.pop()
        else:
            res = -1
        self.check()
        return res
        
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end


# inputs1 = ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# inputs2 = [[], [1], [2], [3], [4], [], [], [], [], []]

# inputs1 = ["FrontMiddleBackQueue","popMiddle","popMiddle","pushMiddle","popBack","popFront","popMiddle"]
# inputs2 = [[],[],[],[8],[],[],[]]

inputs1 = ["FrontMiddleBackQueue","pushMiddle","popMiddle","popFront","popBack","popMiddle","pushMiddle","pushMiddle"]
inputs2 = [[],[8],[],[],[],[],[1],[10]]

obj = FrontMiddleBackQueue()

for i in range(1, len(inputs1)):
    cmd = inputs1[i]
    val = inputs2[i]

    if cmd == 'pushFront':
        obj.pushFront(val[0])
    elif cmd == 'pushBack':
        obj.pushBack(val[0])
    elif cmd == 'pushMiddle':
        obj.pushMiddle(val[0])
    elif cmd == 'popFront':
        print('popFront', obj.popFront())
    elif cmd == 'popMiddle':
        print('popMiddle', obj.popMiddle())
    elif cmd == 'popBack':
        print('popBack', obj.popBack())
