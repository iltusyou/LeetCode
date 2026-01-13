#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacks = []
        res = 0

        for c in tokens:
            print(c)

            if c == "+":
                tmp = stacks[-1] + stacks[-2]
                stacks = stacks[:-2]
                stacks.append(tmp)

            elif c == '-':
                tmp = stacks[-2] - stacks[-1]
                stacks = stacks[:-2]
                stacks.append(tmp)

            elif c == '*':
                tmp = stacks[-1] * stacks[-2]
                stacks = stacks[:-2]
                stacks.append(tmp)

            elif c == '/':
                tmp = int(stacks[-2] / stacks[-1])
                stacks = stacks[:-2]
                stacks.append(tmp)

            else:
                stacks.append(int(c))

            print(stacks)



        return 
        
# @lc code=end

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
ans = sol.evalRPN(tokens)
print(ans)

print(6//-132)


