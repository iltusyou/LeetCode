#
# @lc app=leetcode id=3709 lang=python3
#
# [3709] Design Exam Scores Tracker
#

# @lc code=start

import bisect

class ExamTracker:

    def __init__(self):
        self.prefix_sum = [0]
        self.times = []

    def record(self, time: int, score: int) -> None:        
        self.prefix_sum.append(self.prefix_sum[-1] + score)
        self.times.append(time)
        
    def totalScore(self, startTime: int, endTime: int) -> int:
        i = bisect.bisect_left(self.times, startTime)
        j = bisect.bisect_right(self.times, endTime)
        if j >= len(self.times):
            j-=1
        if self.times[j] > endTime:
            j-=1

        res = self.prefix_sum[j+1] - self.prefix_sum[i]

        print(self.times, self.prefix_sum, startTime, endTime, i, j, res)
        return res
        


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)
# @lc code=end

obj = ExamTracker()

inputs1 = ["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"]
inputs2 = [[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]

ans = []
for i in range(1, len(inputs1)):
    if inputs1[i] == 'record':
        param_2 = obj.record(inputs2[i][0], inputs2[i][1])

    elif inputs1[i] == 'totalScore':
        param_2 = obj.totalScore(inputs2[i][0], inputs2[i][1])

    ans.append(param_2)

print(ans)

    



# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)