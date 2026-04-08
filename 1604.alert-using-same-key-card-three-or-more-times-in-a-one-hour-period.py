#
# @lc app=leetcode id=1604 lang=python3
#
# [1604] Alert Using Same Key-Card Three or More Times in a One Hour Period
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic = defaultdict(list)

        for name, time in zip(keyName, keyTime):            
            dic[name].append(time)

        def get_hour_and_minute(s):
            h, m = s.split(":")
            return (int(h), int(m))


        ans = []
        for name in dic.keys():
            times = sorted(dic[name])
            times = list(map(get_hour_and_minute, times))
          
            for i in range(2, len(times)):
                t1, t2 = times[i-2], times[i]
                h1, m1 = t1
                h2, m2 = t2
                diff = (h2 - h1) * 60 + (m2 - m1)

                if diff <= 60:
                    ans.append(name)
                    break

        ans.sort()        
        return ans
# @lc code=end

keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]

sol = Solution()
ans = sol.alertNames(keyName, keyTime)
print(ans)