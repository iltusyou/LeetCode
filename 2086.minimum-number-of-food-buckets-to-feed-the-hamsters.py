#
# @lc app=leetcode id=2086 lang=python3
#
# [2086] Minimum Number of Food Buckets to Feed the Hamsters
#

# @lc code=start
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters = [c for c in hamsters]        
        n = len(hamsters)

        ans = 0
        for i, x in enumerate(hamsters):
            if x == 'H':
                if i > 0 and hamsters[i-1] == 'F':
                    continue

                if i < n-1 and hamsters[i+1] == '.':
                    hamsters[i+1] = 'F'
                    ans += 1
                elif i > 0 and hamsters[i-1] == '.':
                    hamsters[i-1] = 'F'
                    ans += 1
                else:
                    return -1                                            

        return ans
    
# @lc code=end

hamsters = "H..H"

sol = Solution()
ans = sol.minimumBuckets(hamsters)
print(ans)