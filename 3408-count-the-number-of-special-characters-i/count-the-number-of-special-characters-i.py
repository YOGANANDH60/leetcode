class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        h = set(word)
        count = 0
        for ch in range(26):
            l = chr(ord('a') + ch)
            u = chr(ord('A') + ch)

            if l in h and u in h:
                count += 1 
            
        return count