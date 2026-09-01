class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        if 2 * k + 1 > n:
            return ans

        window = sum(nums[:2 * k + 1])

        for i in range(k, n - k):
            ans[i] = window // (2 * k + 1)

            if i + k + 1 < n:
                window += nums[i + k + 1]
                window -= nums[i - k]

        return ans