class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        cost = 0

        if costBoth < (cost1+cost2):
            mn = min(need1,need2)

            cost += mn * costBoth
            cost +=  (need1 - mn) *min(cost1,costBoth)
            cost += (need2 - mn) *min(cost2,costBoth)

        else:
            cost += (need1 *cost1) + (need2*cost2)

        return cost