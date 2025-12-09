class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sperate = s.split()
        length = len(sperate)
        last = sperate[length-1]
        return len(last)