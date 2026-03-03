#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        que1 = deque(deck)
                
        que2 = deque()
        que2.append(que1.pop())

        while que1:
            que2.appendleft(que2.pop())
            que2.appendleft(que1.pop())

        ans = list(que2)       
        return ans
    
# @lc code=end

deck = [17,13,11,2,3,5,7]
sol = Solution()
ans = sol.deckRevealedIncreasing(deck)
print(ans)
