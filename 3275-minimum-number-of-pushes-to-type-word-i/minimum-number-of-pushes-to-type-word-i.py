class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter

        freq = Counter(word)
        counts = sorted(freq.values(), reverse=True)

        pushes = 0
        for i, c in enumerate(counts):
            pushes += (i // 8 + 1) * c

        return pushes
