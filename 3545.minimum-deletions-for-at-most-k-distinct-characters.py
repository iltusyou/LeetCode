#
# @lc app=leetcode id=3545 lang=python3
#
# [3545] Minimum Deletions for At Most K Distinct Characters
#

# @lc code=start
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        dic = {}

        for c in s:
            dic[c] = dic.get(c, 0) + 1

        arr = [(val, key) for key, val in dic.items()]
        cnt = len(arr)

        if cnt == k:
            return 0                

        arr.sort()  
        ans = sum(x for x,_ in arr[:cnt - k] )
   
       

        print(dic, arr)

        return ans
# @lc code=end

s = "abc"
k = 2

# s = "aabb"
# k = 2

sol = Solution()
ans = sol.minDeletion(s, k)
print(ans)