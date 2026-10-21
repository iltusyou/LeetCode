#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for x in s:
            if x == '(':
                stack.append(x)
            else:
                last = stack.pop()

                if last == '(':
                    stack.append(1)
                else:
                    stack.pop()
                    stack.append(last * 2)

                if len(stack) >= 2 and isinstance(stack[-2] , int):
                    stack.append(stack.pop() + stack.pop())

            # print(x, stack)
                                                                                            
        return stack[0]
    
# @lc code=end

s = "(())"
sol = Solution()
ans = sol.scoreOfParentheses(s)
print(ans)

