class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        m = (c // 2) + 1

        l = 0
        r = int(c**0.5)
        while l <= r:
            if l**2 + r **2 == c:
                return True
            elif l**2 + r**2 < c:
                l +=1
            else:
                r -=1 
        return False