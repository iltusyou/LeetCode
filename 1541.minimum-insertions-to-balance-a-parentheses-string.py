#
# @lc app=leetcode id=1541 lang=python3
#
# [1541] Minimum Insertions to Balance a Parentheses String
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        stack = [] 

        ans = 0
        for c in s:
            if c == '(':
                if stack and stack[-1] == ')':
                    stack.pop()
                    stack.pop()
                    ans += 1                    
                
                stack.append(c)

            else:
                if not stack:
                    stack.append('(')
                    stack.append(c)
                    ans += 1
                elif stack[-1] == ')':
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(c)

            print(stack, ans)

        if stack and stack[-1] == ')':
            stack.pop()
            stack.pop()
            ans += 1

        print(stack, ans)
    
        ans += len(stack)*2
            
        return ans
# @lc code=end

# s = "(()))"
# s= "))())("
# s = "()()()()()("
s = "))())("

sol = Solution()
ans = sol.minInsertions(s)
print(ans)