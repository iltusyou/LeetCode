#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        count20 = 0

        for i in range(0, len(bills)):
            if bills[i] == 5:
                count5 += 1
            
            elif bills[i] ==10:
                if count5 > 0:
                    count5 -=1
                    count10 +=1            
                else:
                    return False
            else:
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                    count20 +=1
                
                elif count5 >= 3:
                    count5 -= 3
                    count20 += 1
                
                else:
                    return False            
                
        return True
# @lc code=end

# bills = [5,5,5,10,20]
bills = [5,5,5,20,10,10]

sol = Solution()
ans = sol.lemonadeChange(bills)
print(ans)
