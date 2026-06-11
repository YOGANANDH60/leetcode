class Solution:
    def maxFreqSum(self, s: str) -> int:
        vfreq = {}
        cfreq = {}
        ch = s.lower()
        for i in ch:
            if i in 'aeiou':
                vfreq[i] = vfreq.get(i,0) + 1
            else:
                cfreq[i] = cfreq.get(i,0) + 1
        return (max(vfreq.values()) if vfreq else 0) + (max(cfreq.values()) if cfreq else 0)