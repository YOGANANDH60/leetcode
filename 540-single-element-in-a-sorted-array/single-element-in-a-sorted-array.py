class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 1:
        #     return nums[0]
        s = 0
        l = len(nums) -1
        while s < l:
            mid = (s+l) // 2
            if mid % 2 == 1:
                mid -=1
            if nums[mid] == nums[mid+1]:
                s = mid + 2
            else:
                l = mid

        return nums[s]
        