class Solution:


    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        for i in range(0, len(s), 2*k):
            sub=s[i:i+(2*k)]
            r=sub[0:k][::-1] + sub[k:2*k]
            print(r)
            res+=r

                  
        return res
    

s = "Thequickbrownfoxjumpsoverthelazydog"
k = 3
# "bacdfeg"

sol = Solution()
print(sol.reverseStr(s,k))

# abcdefg 
# bacdefg
# cabdefg