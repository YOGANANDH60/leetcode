class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort()
        ans = 0
        cu = 0
        n = len(satisfaction) - 1
        while n >=0:
            cu += satisfaction[n]
            if cu<0:
                break
            ans += cu
            n -=1
        return ans

        