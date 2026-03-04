#
# @lc app=leetcode id=1845 lang=python3
#
# [1845] Seat Reservation Manager
#

# @lc code=start
import heapq


class SeatManager:

    def __init__(self, n: int):
        h = [ i+1 for i in range(n)]    
        self.h = h            

    def reserve(self) -> int:        
        return heapq.heappop(self.h)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h, seatNumber)      

       


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end


inputs1 = ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
inputs2 = [[5], [], [], [2], [], [], [], [], [5]]

obj = SeatManager(inputs2[0][0])
for i in range(1, len(inputs2)):
    if inputs1[i] == 'reserve':
        param_1 = obj.reserve()
        print(param_1)
    if inputs1[i] == 'unreserve':
        seatNumber = inputs2[i][0]
        print(obj.unreserve(seatNumber))

# param_1 = obj.reserve()
# obj.unreserve(seatNumber)