class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        h = {}
        for i in range(nums[0],nums[-1]+1):
            h[i]= h.get(i,0)

        for j in nums:
            h[j]= h.get(j,0) + 1

        a = []
        for k,v in h.items():
            if v== 0:
                a.append(k)
        a.sort()
        return a

        