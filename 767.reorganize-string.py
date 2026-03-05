#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
from itertools import chain


class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0)+1

        sorted_d = sorted([[k, d[k]] for k in d], key= lambda x:x[1], reverse= True) 

        longest_len = sorted_d[0][1] #最長的次數
        other = [(c, t) for i,(c, t) in  enumerate(sorted_d) if i != 0] #其他的
        other_len_sum = sum([ t for (c, t) in other])        

        if longest_len - other_len_sum > 1:
            return ''    

        ans = [[sorted_d[0][0]] for _ in range(longest_len)]
        i = 0
        for c, t in other:            
            for j in range(t):                
                ans[i].append(c)
                i += 1
                if i == longest_len:
                    i = 0                
        
        return ''.join(list(chain.from_iterable(ans))) 
    
# @lc code=end


s = "aab"
# s = "aaab"

sol = Solution()
ans = sol.reorganizeString(s)
print(ans)