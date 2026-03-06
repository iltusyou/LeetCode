#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start

class Node:
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            print(cur.son)

            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]        
        cur.end = True

    def find(self, word: str) -> int:
        cur = self.root        
        for c in word:            
            if c not in cur.son:
                return 0            
            cur = cur.son[c]
        return 1 if cur.end else 2
    
    def search(self, word: str) -> bool:        
        return self.find(word) == 1
        
    def startsWith(self, prefix: str) -> bool:              
        return self.find(prefix) > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

obj = Trie()

# input1 = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# input2 = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

input1 = ["Trie","insert","search","startsWith"]
input2 = [[],["a"],["a"],["a"]]

ans = [None]

for op, val in zip(input1, input2):
    if op == 'insert':
        word = val[0]
        ans.append(obj.insert(word))
        continue

    if op == 'search':
        word = val[0]
        param_2 = obj.search(word)
        ans.append(param_2)
        continue

    if op == 'startsWith':
        prefix = val[0]
        param_3 = obj.startsWith(prefix)
        ans.append(param_3)
        continue

print(ans)

