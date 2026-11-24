class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        h = max(candies)
        for i in candies:
            if (i + extraCandies) >= h:
                result.append(True)
            else:
                result.append(False)

        return result
