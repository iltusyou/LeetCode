#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

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

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:        
        cur = self.root
        
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()                     
            cur = cur.son[c]
                               
        cur.end = True     

            
    def search(self, word: str) -> bool:

        def dfs(w: str, node: Node):            
        
            c = w[0]

            if len(w) == 1:
                
                if c == '.':                    
                    return any(n.end for k, n in node.son.items())

                else:                         
                    return c in node.son and node.son[c].end
            
            if c == '.':

                for k, n in node.son.items():
                    find = dfs(w[1:], n)
                    if find:
                        return True                                    
                return False
            
            elif c not in node.son:
                return False
            
            else:                
                return dfs(w[1:], node.son[c])

        ans = dfs(word, self.root)
             
        return ans


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end



# input1 = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# input2 = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

input1 = ["WordDictionary","addWord","addWord","search"]
input2 = [[],["a"],["a"],[".a"]]

ans = [None]
for op, word in zip(input1, input2):
    if op == 'addWord':
        ans.append(obj.addWord(word[0]))
        continue
    if op == 'search':
        ans.append(obj.search(word[0]))
        continue

print(ans)
