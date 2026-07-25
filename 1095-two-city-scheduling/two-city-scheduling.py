class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        c = []
        for i in range(len(costs)):
            deff = costs[i][0] - costs[i][1]
            c.append((deff,costs[i][0],costs[i][1]))

        c.sort()
        ans = 0
        for i in range(len(c)//2):
            ans += c[i][1]

        for i in range(len(c)//2,len(c)):
            ans += c[i][2]
        return ans