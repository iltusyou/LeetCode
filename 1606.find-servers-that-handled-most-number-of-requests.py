#
# @lc app=leetcode id=1606 lang=python3
#
# [1606] Find Servers That Handled Most Number of Requests
#

# @lc code=start
import heapq


class Solution:
    def build(self, node, start, end):
        
        if start == end:
            self.free[node] = 1

        else:
            mid = (start + end) // 2
            left = self.build(node * 2, start, mid)
            right = self.build(node * 2 + 1, mid+1, end)
            self.free[node] = left + right        

        return self.free[node]

    def update(self, node, start, end, index, val):
        if start == end:
            self.free[node] = val
            return val

        mid = (start + end) // 2
        if index <= mid:
            self.update(node * 2, start, mid, index, val)
        else:
            self.update(node*2+1, mid+1, end, index, val)

        self.free[node] = self.free[node*2] + self.free[node*2+1]
        return self.free[node]

    def query(self, node, start, end, index):
        stack = []
        stack.append((node, start, end))

        while stack:            
            n, s, e = stack.pop()

            if s == e:
                return s

            mid = (s + e) // 2
            l = (n*2, s, mid)
            r = (n*2+1, mid+1, e)
                        
            if self.free[n*2] > 0:
                if index < mid:
                    stack.append(l)
                elif index <= mid:
                    stack.append(l)             
            if self.free[n*2+1] > 0 and mid < index:
                stack.append(l)                    

        stack.append((node, start, end))                                                                    
                
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        
        self.free = [0] * (4 * k)        
        busy = []

        handled = [0] * k

        self.build(1, 0, k-1)        
        # print(self.free)

        start, end = 0, k-1

        for i, time in enumerate(arrival):
           
            while busy and busy[0][0] <= time:
                f = heapq.heappop(busy)
                self.update(1, start, end, f[1], 1)

            # print(i, time, self.free, busy)

            if self.free[1] == 0:               
                continue

            index = i % k

            server_id = self.query(1, start, end, index)                        
            finish_time = time + load[i]

            self.update(1, start, end, server_id, 0)
            heapq.heappush(busy, (finish_time, server_id))

            handled[server_id] += 1

            # print(i, time, server_id, self.free, busy)

        max_handled = max(handled)
        ans = [i for i, x in enumerate(handled) if x == max_handled]
        return ans     
    
# @lc code=end

k = 3
arrival = [1,2,3,4,5]
load = [5,2,3,3,3] 

# k = 1
# arrival = [1]
# load = [1]

sol = Solution()
ans = sol.busiestServers(k, arrival, load)
print(ans)