from typing import List

class Solution:
    def getHashFromNums(self, nums):
        hash = {}
        for n in nums:
            if n not in hash:
                hash[n] = True

        return hash

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = self.getHashFromNums(nums1)
        hash2 = self.getHashFromNums(nums2)

        for key in list(hash1.keys()):
            if key not in hash2:
                hash1.pop(key)        

        res = list(hash1.keys())    
        return res



nums1 = [1,2,2,1]
nums2 = [2,2]

s = Solution()
print(s.intersection(nums1, nums2))