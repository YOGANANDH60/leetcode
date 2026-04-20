class Solution:
    def topKFrequent(self, li: List[int], k: int) -> List[int]:
        fre = {}
        val = []

        for i in li:
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1
        freq = dict(sorted(fre.items(),key=lambda x:x[1],reverse=True))

        for i, key in enumerate(freq):
            if i == k:
                break
            val.append(key)

        return val
        