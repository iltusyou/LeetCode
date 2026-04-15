#
# @lc app=leetcode id=1053 lang=python3
#
# [1053] Previous Permutation With One Swap
#

# @lc code=start
from typing import List


class Solution:
    def swap(self, arr: List[int], i: int, j: int) -> List[int]:        
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        return arr

    def prevPermOpt1(self, arr: List[int]) -> List[int]:        
        n = len(arr)        

        if n == 1:
            return arr
      
        stacks = [(n-1, arr[n-1])] 

        for i in range(n-2, -1, -1):        
            
            if arr[i] > stacks[-1][1]:   
                a = arr[i]
                ops = [(i, v) for i, v in stacks if v < a]       
                print(stacks, ops)
                return self.swap(arr, i, ops[0][0])                            

            elif stacks[-1][1] == arr[i]:
                stacks.pop()                                                                           
                       
            stacks.append((i, arr[i]))

            print(i, arr[i], stacks)
                      
        return arr
    
# @lc code=end

# arr = [1,1,5]
# arr = [1,9,4,6,7]
arr = [3,1,1,3]

sol = Solution()
ans = sol.prevPermOpt1(arr)
print(ans)
