#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#

# @lc code=start
from typing import List

def print_trie(node, prefix=""):
    if node.end:
        print(prefix)
    for char, child in node.son.items():
        print_trie(child, prefix + char)

class Node:
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False
        self.word_len = 0

class MagicDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]                    
        cur.end = True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.addWord(word)
        
        print_trie(self.root)

    def search(self, searchWord: str) -> bool:
                
        def dfs(word: str, node:Node, fail_match: int):                                                       

            if fail_match > 1:
                return False

            if len(word) == 0:
                return node.end and fail_match == 1
                                    
            for k, n in node.son.items():                
                cur_match = k == word[0]
                if not cur_match:
                    fail_match += 1
                               
                res = dfs(word[1:], n, fail_match)
                if res:
                    return True
                
                if not cur_match:
                    fail_match -= 1

            return False
            
        return dfs(searchWord, self.root, 0)                


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end

input1 = ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
input2 = [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]

for op, dic in zip(input1, input2):
    if op == 'buildDict':
        obj.buildDict(dic[0])
        continue

    if op == 'search':
        param_2 = obj.search(dic[0])
        print('search', dic[0], param_2)
        continue
