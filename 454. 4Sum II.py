from typing import List


class Solution:          
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash = {}
        for a in nums1:
            for b in nums2:
                hash[a+b] = hash.get(a+b, 0) + 1

        count = 0
        for c in nums3:
            for d in nums4:
                key = -(c+d)
                if key in hash:
                    count+=hash[key]
                                     
        return count
    

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

# nums1 = [1]
# nums2 = [-1]
# nums3 = [0]
# nums4 = [1]

# nums1 = [0]
# nums2 = [0]
# nums3 = [0]
# nums4 = [0]

# nums1 = [-1,-1]
# nums2 = [-1,1]
# nums3 = [-1,1]
# nums4 = [1,-1]

s = Solution()
print(s.fourSumCount(nums1, nums2, nums3, nums4))

