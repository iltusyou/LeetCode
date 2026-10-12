class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:        
        min_dist, ans = float('inf'), -1

        for i, x in enumerate(drones):
            dist = abs(x[0] - target[0]) + abs(x[1] - target[1])

            if dist < min_dist and dist <= x[2]:
                min_dist = dist
                ans = i

        return ans



# drones = [[0,0,8],[2,2,9]]
# target = [3,4]

drones = [[2,9,3],[-25,0,15]]
target = [-25,-15]

s = Solution()
ans = print(s.nearestDrone(drones, target))