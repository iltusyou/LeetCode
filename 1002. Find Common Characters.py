from typing import List


class Solution:
    def getDicFromWord(self, word:str)->dict:
        dic={}
        for w in word:
            if w in dic:
                dic[w]+=1
            else:
                dic[w]=1
        return dic
    
    def compareDic(self, dic1:dict, dic2:dict)->dict:
        for key in list(dic1.keys()) :
                        
            if key not in dic2:
                dic1.pop(key)
            
            else: 
                dic1[key] = min(dic1[key], dic2[key])
                    
        return dic1
        

    def commonChars(self, words: List[str]) -> List[str]:
        dic = self.getDicFromWord(words[0])
         
        for i in range(1, len(words)):        
            tmpDic = self.getDicFromWord(words[i])
            dic = self.compareDic(dic, tmpDic)

        res = []
        for k in dic.keys():
            for i in range(0, dic[k]):
                res.append(k)
        
        return res

words = ["bella","label","roller"]
# Output: ["e","l","l"]

s = Solution()
# s.commonChars(words)
print(s.commonChars(words))