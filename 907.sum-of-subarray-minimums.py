#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
from collections import deque


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        que = deque()

        ans = 0
        accu_sum = 0
        for x in arr:
            if que and x == que[-1][0]:
                que[-1] = (que[-1][0], que[-1][1] + 1)
                accu_sum += x

            else:
                cnt = 1                        
                while que and x < que[-1][0]:                                
                    
                    n, c = que.pop()
                    cnt += c
                    accu_sum -=  n * c
                
                que.append((x, cnt))        
                accu_sum += que[-1][0] * que[-1][1]

            ans += accu_sum           

            # print(x, que, accu_sum, ans)

        ans = ans % (10 ** 9 + 7)

        return ans
# @lc code=end

# arr = [3,1,2,4]
# arr = [11,81,94,43,3]
arr = [20000,20000,20000,20000,20000,1]
# arr = [3, 2, 1]

sol = Solution()
ans = sol.sumSubarrayMins(arr)
print(ans)