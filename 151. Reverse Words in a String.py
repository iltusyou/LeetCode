class Solution:
    def reverseWords(self, s: str) -> str:        

        r = s.split( )[::-1]
        res = " ".join(r)
        return res

        

        
    
s = "  hello world  "
sol = Solution()
print(sol.reverseWords(s))