class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for ii in range(n):
            for j in range(ii+1,n):
                if nums[ii] +nums[j] == target:
                    return [ii,j]
        
