#
# @lc app=leetcode id=1366 lang=python3
#
# [1366] Rank Teams by Votes
#

# @lc code=start
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]
        
        dic = {}

        for vote in votes:
            for i, x in enumerate(vote):                                
                if x not in dic:
                    dic[x] = [0 for _ in range(26)]
                    dic[x].append(ord('Z') - ord(x))

                dic[x][i] += 1                

        sorted_dic = sorted([v for v in dic.values()], reverse= True) 
        ans = ''.join([chr(ord('Z') - d[26]) for d in sorted_dic])                                                

        return ans
    
# @lc code=end
# votes = ["ABC","ACB","ABC","ACB","ACB"]
# votes = ["WXYZ","XYZW"]
votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]

sol = Solution()
ans = sol.rankTeams(votes)
print(ans)
