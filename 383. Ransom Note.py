class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCount = [0]*26
        magazineCount = [0]*26

        for c in ransomNote:
            i = ord(c) - ord('a')
            ransomNoteCount[i]+=1

        for c in magazine:
            i = ord(c) - ord('a')
            magazineCount[i]+=1
        
        for i in range(0, len(ransomNoteCount)):
            if magazineCount[i] < ransomNoteCount[i]:
                return False
  

        return True
    


ransomNote = "a"
magazine = "b"

s = Solution()
r = s.canConstruct(ransomNote, magazine)
print(r)