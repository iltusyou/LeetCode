#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def backtracking(self, left: int, right: int, s: str, index: int, path: str, result: set, maxLength: list[int]):        
        # print(left, right, s, index, path, result, maxLength)
        
        if index == len(s):
            if left == right:          
                l = len(path)
                
                if l > maxLength[0]:                               
                    maxLength[0] = l                    
                    result.clear()
                    
                if l >= maxLength[0]:
                    result.add(path)                                
            return

        if right > left:
            return

        self.backtracking(left, right, s, index+1, path, result, maxLength)

        cur = s[index]
        path += cur
        if cur == '(':
            left += 1
        if cur == ')':
            right += 1

        self.backtracking(left, right, s, index+1, path, result, maxLength)

        return

    def removeInvalidParentheses(self, s: str) -> list[str]:
        if '(' not in s or ')' not in s:
            s = s.replace('(', '').replace(')', '')
            return [s]

        s = s.rstrip('(')
        s = s.lstrip(')')

        res = set()
        
        self.backtracking(0, 0, s, 0, '', res, [0])
   
        return list(res)
            

        
# @lc code=end

s = "()())()"
# s = "(a)())()"
# s = ")("
# s = "(()"

# s = "(()()))q(l)()o)(z"
# s = ")t))()()bo)" #["t(()bo)","t()(bo)","t()()bo"]

sol = Solution()
ans = sol.removeInvalidParentheses(s)
print(ans)

