class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        romanno= {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
        n = len(s)
        total = 0
        for i in range(n):
            if i < n-1 and romanno[s[i]] < romanno[s[i+1]]:
                total -= romanno[s[i]]
            else:
                total += romanno[s[i]]
        return total
        