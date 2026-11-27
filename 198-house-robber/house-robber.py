class Solution:
    def rob(self, nums: list[int]) -> int:
        pre,cur = 0,0
        for i in nums:
            pre,cur = cur,max(cur,pre+i)

        return cur