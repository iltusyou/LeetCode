#
# @lc app=leetcode id=1540 lang=python3
#
# [1540] Can Convert String in K Moves
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if s == t:
            return True
            
        if len(s) != len(t):
            return False
        
        moves = defaultdict(int)

        for x, y in zip(s, t):        
            key = ord(y) - ord(x)
            if key < 0:
                key += 26
            moves[key] += 1

        sorted_moves = sorted([[v, k] for k, v in moves.items() if k > 0], reverse = True) 
       
        max_moves = (sorted_moves[0][0] - 1) * 26 + sorted_moves[0][1]
        ans = max_moves <= k

        print(moves, sorted_moves, max_moves)

        return ans
# @lc code=end

# s = "input"
# t = "ouput"
# k = 9

# s = "abc"
# t = "bcd"
# k = 10

# s = "aab"
# t = "bbb"
# k = 27

# s = "leetcode"
# t = "leetcode"
# k = 0

# s = "abc"
# t = "abcd"
# k = 1000

s = "atmtxzjkz"
t = "tvbtjhvjd"
k = 35

sol = Solution()
ans = sol.canConvertString(s, t, k)
print(ans)