class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        max_length = len(max(strs))
        i = 0
        while i < max_length:
            common = strs[0][:i + 1]
            for s in strs:
                if i < len(s) and s[:i + 1] == common:
                    continue
                else:
                    return res
            res = common
            i += 1

        return res