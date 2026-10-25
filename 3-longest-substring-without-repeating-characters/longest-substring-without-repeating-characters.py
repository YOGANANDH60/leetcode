class Solution:
    def lengthOfLongestSubstring(self, n: str) -> int:
        hm = {}
        l = 0

        ml = 0
        for i in range(len(n)):
            if n[i] in hm and hm[n[i]] >= l: 
                l = hm[n[i]] + 1
            hm[n[i]] = i
            ml = max(ml,i-l+1)
        
        return ml