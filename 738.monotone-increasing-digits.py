#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#

# @lc code=start
class Solution:
    def nToNums(self, n: int):
        nums = []
        while n >= 10:
            nums.append(n % 10)
            n = n//10        

        nums.append(n)
        nums.reverse()
        return nums
    
    def findHasmonotoneDecreasingStart(self, nums):
        start = 0
        for i in range(0, len(nums)-1):            
            if nums[i] < nums[i+1]:                
                start = i + 1

            if nums[i] > nums[i+1]:
                return start
            
        return None

    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = self.nToNums(n)          
        start = self.findHasmonotoneDecreasingStart(nums)

        if start is None:            
            return n

        nums[start] -= 1        
        for i in range(start+1, len(nums)):
            nums[i] = 9

        if nums[0] == 0:
            nums.pop(0)        
        nums.reverse() 

        res = 0
        for i in range(len(nums)-1, -1, -1):       
            res += nums[i] * (10 ** i)

        return res
        
# @lc code=end

# n = 10
n = 1234
# n = 332 # 299
# n = 1000
# n = 101
# n = 67890

sol = Solution()
ans = sol.monotoneIncreasingDigits(n)
print(ans)
