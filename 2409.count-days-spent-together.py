#
# @lc app=leetcode id=2409 lang=python3
#
# [2409] Count Days Spent Together
#

# @lc code=start
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def toNum(s: str):
            s = s.replace('-', '')
            return int(s)

        arriveMax = max(toNum(arriveAlice), toNum(arriveBob))
        leaveMin = min(toNum(leaveAlice), toNum(leaveBob))

        if arriveMax > leaveMin:
            return 0

        arrive = (arriveMax//100, arriveMax%100)
        leave = (leaveMin//100, leaveMin%100)
        
        if arrive[0] == leave[0]:
            return leave[1] - arrive[1] + 1

        ans = 0
        for i in range(arrive[0]-1, leave[0]-1):
            ans += months[i]        

        ans = ans - arrive[1] + leave[1] + 1

        return ans


        

        
        
# @lc code=end

# arriveAlice = "08-15"
# leaveAlice = "08-18"
# arriveBob = "08-16"
# leaveBob = "08-19"

arriveAlice = "08-31"
leaveAlice = "09-01"
arriveBob = "08-31"
leaveBob = "09-01"

sol = Solution()
ans = sol.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
print(ans)
