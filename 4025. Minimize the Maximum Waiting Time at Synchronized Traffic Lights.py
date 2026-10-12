class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        light = max(lights)
        ans = 0

        for x in arrivalTime:
            r = x % period

            if r >= light:
                ans = max(period - r, ans)

        return ans

period = 8
lights = [2,3]
arrivalTime = [2,5,8,11]

sol = Solution()
ans = sol.minPenalty(period, lights, arrivalTime)
print(ans)