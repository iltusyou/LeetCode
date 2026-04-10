#
# @lc app=leetcode id=2232 lang=python3
#
# [2232] Minimize Result by Adding Parentheses to Expression
#

# @lc code=start
class Solution:
    def minimizeResult(self, expression: str) -> str:        
        left, right = expression.split('+')
        print(left, right)

        def str_to_int(s):
            return int(s) if s else 1
        
        def cal(s1, s2, s3, s4):
            n1 = str_to_int(s1)
            n2 = str_to_int(s2)
            n3 = str_to_int(s3)
            n4 = str_to_int(s4)
            return n1 * (n2 + n3) * n4

        
        min_val, ans = float('inf'), ''

        for i in range(len(left)):
            for j in range(len(right)):
                
                s1 = left[:i]
                s2 = left[i:]
                s3 = right[:j+1]
                s4 = right[j+1:]

                val = cal(s1, s2, s3, s4)                

                if val < min_val:                    
                    ans = f"{s1}({s2}+{s3}){s4}"
                    min_val = val
                
        return ans
# @lc code=end

expression = "247+38"

sol = Solution()
ans = sol.minimizeResult(expression)
print(ans)