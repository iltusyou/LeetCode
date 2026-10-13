#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans, tmp = '', ''
        for c in s:            
            tmp += c

            if c == ')':
                stack.pop()

                if not stack:
                    ans += tmp[1:-1]
                    tmp = ''
            else:
                stack.append(c)   

            # print(f"tmp {tmp}, ans {ans}")         

        return ans
# @lc code=end

s = "(()())(())"

sol = Solution()
ans = sol.removeOuterParentheses(s)
print(ans)