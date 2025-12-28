class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = Counter(nums)

        for i in v:
            if v[i] == 1:
                return i
        