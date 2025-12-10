class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            f = len(str(nums[i]))
            if(f%2==0):
                count +=1
        return count
        