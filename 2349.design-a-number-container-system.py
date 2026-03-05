#
# @lc app=leetcode id=2349 lang=python3
#
# [2349] Design a Number Container System
#

# @lc code=start
import bisect
from collections import defaultdict
import heapq


class NumberContainers:

    def __init__(self):
        self.idoc = {} #index 為 key 
        self.ndoc = defaultdict(list) #number 為key 紀錄出現index

    def change(self, index: int, number: int) -> None:             
        self.idoc[index] = number
        heapq.heappush(self.ndoc[number], index)
    

    def find(self, number: int) -> int:
        arr = self.ndoc[number]

        while arr and self.idoc[arr[0]] != number:
            heapq.heappop(arr)  
        
        return arr[0] if arr else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end

obj = NumberContainers()

inputs1 = ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
inputs2 = [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]

null = None
# inputs1 = ["NumberContainers","change","change","change","find","change","find","find","change","find","find","find","change","find","change","change","find","find","change","find","change","change","find","find","find","change","find","find","change","find","find","find","change","find","change","change","find","change","change","change","change","find","change","change","find","change","find","find","change","change","find","change","find","change","change","find","change","change","find","change","find","change","find","find","find","change","find","find","change","change","find","change","change","find","change","change","find","find","change","find","change","change","find","find","find","find","change","find","change","find","change","change","find","change","find","change","change","change","change","find","find","find","change","change","change","change","change","find","change","change","change","find","change","change","find","change","change","find","change","change","change","change","change","change","find","find","find","find","change","find","find","find","find","change","find","change","find","find","find","find","change","find","find","change","find","find","change","change","change","change","change","change","find","find","change","change","change","change","find","change","change","change","change","change","change","change","change","find","change","find","change","find","change","change","change","change","find","change","find","change","change","change","change","change","change","change","change","change","change","find","change","change","find","change","change","change","find","find","change","find","find"]
# inputs2 = [[],[158,9],[75,85],[75,187],[77],[109,113],[184],[77],[17,191],[113],[35],[184],[164,119],[9],[19,151],[142,50],[77],[85],[35,164],[184],[118,164],[3,164],[184],[113],[135],[72,105],[9],[187],[34,105],[135],[164],[135],[20,164],[187],[158,184],[44,50],[191],[164,50],[20,191],[158,191],[107,113],[187],[158,50],[142,9],[151],[35,119],[113],[105],[127,77],[164,164],[187],[72,191],[113],[132,164],[7,9],[85],[71,187],[7,187],[9],[20,185],[35],[7,151],[119],[135],[77],[155,187],[164],[135],[183,151],[110,164],[50],[20,85],[19,9],[85],[175,9],[116,105],[187],[164],[107,35],[185],[147,184],[109,184],[35],[184],[187],[113],[178,85],[9],[178,151],[85],[107,164],[116,135],[113],[107,164],[77],[116,35],[172,35],[200,187],[142,50],[50],[187],[105],[127,9],[34,164],[178,135],[183,50],[34,35],[184],[147,77],[172,35],[132,151],[119],[7,185],[109,185],[187],[110,135],[175,35],[35],[127,187],[71,164],[188,9],[35,50],[107,191],[158,119],[85],[50],[35],[77],[183,164],[119],[9],[77],[50],[164,9],[151],[172,77],[50],[135],[113],[77],[200,9],[77],[184],[142,105],[119],[9],[75,185],[142,113],[127,119],[110,85],[7,135],[127,185],[185],[77],[200,50],[164,164],[19,35],[172,113],[135],[178,35],[72,35],[142,85],[3,113],[109,151],[110,77],[35,119],[75,164],[105],[142,113],[164],[127,105],[119],[110,135],[158,35],[35,164],[35,9],[135],[178,50],[119],[73,185],[19,85],[155,151],[44,187],[116,191],[158,35],[110,191],[72,187],[7,9],[17,135],[35],[200,185],[142,185],[164],[175,187],[188,185],[172,50],[9],[119],[110,191],[35],[35]]
# Expected = [null,null,null,null,-1,null,-1,-1,null,109,-1,-1,null,158,null,null,-1,-1,null,-1,null,null,-1,109,-1,null,158,75,null,-1,3,-1,null,75,null,null,17,null,null,null,null,75,null,null,19,null,107,34,null,null,75,null,107,null,null,-1,null,null,142,null,-1,null,35,-1,127,null,3,-1,null,null,44,null,null,20,null,null,71,3,null,-1,null,null,107,109,71,-1,null,19,null,20,null,null,-1,null,127,null,null,null,null,44,71,34,null,null,null,null,null,109,null,null,null,35,null,null,71,null,null,34,null,null,null,null,null,null,20,35,34,147,null,158,19,147,35,null,132,null,35,110,-1,147,null,147,-1,null,158,19,null,null,null,null,null,null,75,147,null,null,null,null,7,null,null,null,null,null,null,null,null,-1,null,71,null,35,null,null,null,null,7,null,-1,null,null,null,null,null,null,null,null,null,null,34,null,null,71,null,null,null,7,-1,null,34,34]

ans = [None]

for i in range(1, len(inputs2)):
    if inputs1[i] == 'change':
        index = inputs2[i][0]
        number = inputs2[i][1]
        obj.change(index,number)
        ans.append(None)
    elif inputs1[i] == 'find':
        number = inputs2[i][0]
        param_2 = obj.find(number)        
        # if(param_2 != Expected[i]):
        #     print(number, param_2, Expected[i])

        # ans.append(param_2)

# print(ans)

