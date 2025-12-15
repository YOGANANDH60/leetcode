class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total = n*(n+1) //2

        mis = total -sum(nums)
        return mis