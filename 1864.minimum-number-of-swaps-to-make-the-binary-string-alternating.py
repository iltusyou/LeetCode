#
# @lc app=leetcode id=1864 lang=python3
#
# [1864] Minimum Number of Swaps to Make the Binary String Alternating
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = defaultdict(int)
        cnt_even = defaultdict(int) #出現在index為偶數的數量        

        for i, x in enumerate(s):
            cnt[x] += 1
            if i % 2 == 0:
                cnt_even[x] += 1

        print(cnt, cnt_even)

        if abs(cnt['0'] - cnt['1']) > 1:
            return -1            

        if cnt['0'] == cnt['1']:
            return min(cnt_even['0'], cnt_even['1'])
        elif cnt['0'] > cnt['1']:
            return cnt_even['1']
        else:
            return cnt_even['0']

# @lc code=end

s = "111000"
# s = "1110"

sol = Solution()
ans = sol.minSwaps(s)
print(ans)