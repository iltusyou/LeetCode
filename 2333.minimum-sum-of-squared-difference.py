#
# @lc app=leetcode id=2333 lang=python3
#
# [2333] Minimum Sum of Squared Difference
#

# @lc code=start
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        arr = [abs(x-y) for (x, y) in zip(nums1, nums2)]
        arr = sorted(arr, reverse = True)
        k = k1 + k2
        n = len(arr)

        if k == 0:
            return sum(a ** 2 for a in arr)

        if sum(arr) <= k:
            return 0
        
        # print(k, arr)        
      
        lower_idx = n-1

        for i in range(1, len(arr)):            
            curr = (arr[i-1] - arr[i]) * (i)
            
            if k - curr <=0:
                lower_idx = i-1
                break

            k -= curr
            
        lower = arr[lower_idx]
        # print(f"k, lower_idx, lower = {k, lower_idx, lower}")

        for i in range(lower_idx):
            arr[i] = lower

        # print(arr)


        quot = (int)(k / (lower_idx+1))
        rem = k % (lower_idx+1)


        # print(quot, rem, arr)

        ans = ((arr[0]-quot -1)**2) * rem
        
        ans += ((arr[rem] - quot)**2) * (lower_idx+1-rem)
        # print(arr)
         
        ans += sum(a ** 2 for a in arr[lower_idx+1:])
        return ans
    
# @lc code=end

# nums1 = [1,2,3,4]
# nums2 = [2,10,20,19]
# k1 = 0
# k2 = 0

nums1 = [1,4,10,12]
nums2 = [5,8,6,9]
k1 = 1
k2 = 1

# nums1 = [11,12,13,14,15]
# nums2 = [13,16,16,12,14]
# k1 = 3
# k2 = 6
# Expected 43

# nums1 = [19,18,19,18,18,19,19]
# nums2 = [1,0,1,0,0,1,1]
# k1 = 10
# k2 = 33


sol = Solution()
ans = sol.minSumSquareDiff(nums1, nums2, k1, k2)
print(ans)