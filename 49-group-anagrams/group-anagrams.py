class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grp = {}
        for word in strs:
            key ="".join(sorted(word))
            grp.setdefault(key, []).append(word)
        return list(grp.values())