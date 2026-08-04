class Solution(object):
    def makeGood(self, ss):
        """
        :type s: str
        :rtype: str
        """
        s = []
        for i in ss:
            if s and s[-1] != i and s[-1].lower() == i.lower():
                s.pop()

            else:
                s.append(i) 
        return "".join(s)
        