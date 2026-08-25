class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        if nums == k:
            return k
        multi = []
        for i in range(1,len(nums)+2):
            multi.append(i*k)

        j = 0
        while j<=len(multi):
            if len(multi) == 1 and multi[0] == nums[0]:
                break
            if multi[j] not in nums:
               break
            j+=1
        return multi[j]
        