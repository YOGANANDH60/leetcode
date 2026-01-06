class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        max_freq = 0
        ans = None

        for key, value in freq.items():
            if value > max_freq:
                max_freq = value
                ans = key

        return  ans
        
        