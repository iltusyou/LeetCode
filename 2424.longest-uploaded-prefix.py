#
# @lc app=leetcode id=2424 lang=python3
#
# [2424] Longest Uploaded Prefix
#

# @lc code=start
import bisect


class LUPrefix:

    def __init__(self, n: int):
        self.x = 1
        self.s = set()

    def upload(self, video: int) -> None:                                             
        self.s.add(video)
        
    def longest(self) -> int:                
        while self.x in self.s:
            self.x += 1

        return self.x - 1
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
# @lc code=end

# input1 = ["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
# input2 = [[4], [3], [], [1], [], [2], []]

# input1 = ["LUPrefix","longest","upload","longest","upload","longest"]
# input2 = [[5],[],[1],[],[5],[]]

input1 = ["LUPrefix","upload","upload","longest","upload","longest"]
input2 = [[10],[1],[10],[],[9],[]]

obj = LUPrefix(input2[0][0])

ans = [None]
for op, val in zip(input1, input2):
    if op == 'upload':
        obj.upload(val[0])
        ans.append(None)
    if op == 'longest':
        param_2 = obj.longest()
        ans.append(param_2)

print(ans)