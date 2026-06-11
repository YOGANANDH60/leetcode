class Solution:
    def maxFreqSum(self, s: str) -> int:
        vfreq = {}
        cfreq = {}
        for i in s:
            if i.lower() in 'aeiou':
                vfreq[i] = vfreq.get(i,0) + 1
            else:
                cfreq[i] = cfreq.get(i,0) + 1
        return (max(vfreq.values()) if vfreq else 0) + (max(cfreq.values()) if cfreq else 0)