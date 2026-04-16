class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            d = [0] * 26
            for c in word:
                d[ord(c) - ord('a')] += 1
            result[tuple(d)].append(word)

        return list(result.values())