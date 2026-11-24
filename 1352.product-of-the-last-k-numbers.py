#
# @lc app=leetcode id=1352 lang=python3
#
# [1352] Product of the Last K Numbers
#

# @lc code=start
class ProductOfNumbers:

    def __init__(self):
        self.dp = [1]
        return

    def add(self, num: int) -> None:
        if num == 0:
            self.dp = [1]

        else:
            if self.dp:
                self.dp.append(self.dp[-1] * num)
            else:
                self.dp.append(num)
                  
        return

    def getProduct(self, k: int) -> int:

        l = len(self.dp)
        if k > l-1:            
            return 0
        
        return self.dp[-1] // self.dp[-(k+1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end

inputs = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
params = [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

productOfNumbers = ProductOfNumbers()

ans = []

for i, op in enumerate(inputs):
    if op == 'add':
        ans.append(productOfNumbers.add(params[i][0]))

    if op == 'getProduct':
        ans.append(productOfNumbers.getProduct(params[i][0]))


print(ans)
