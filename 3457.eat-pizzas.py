#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#

# @lc code=start
from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse = True)

        n = len(pizzas)        
        days = n // 4
        odd_cnt = (days + 1) //2 #odd cnt
        even_cnt = days // 2 #even cnt

        arr = pizzas[:odd_cnt]
        end = odd_cnt + 1 + even_cnt * 2
        arr2 = pizzas[odd_cnt+1:end:2]

        ans = sum(arr) + sum(arr2)        

        return ans
    
# @lc code=end

pizzas = [1,2,3,4,5,6,7,8]
# pizzas = [2,1,1,1,1,1,1,1]
# pizzas = [5,2,2,4,3,3,1,3,2,5,4,2]
# pizzas = [3,4,2,4,2,4,2,2,4,5,3,2,1,2,1,1]

sol = Solution()
ans = sol.maxWeight(pizzas)
print(ans)