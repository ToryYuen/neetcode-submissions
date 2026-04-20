from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        need = dict(Counter(s1))

        window = {}
        for c in s2[:len(s1)]:
            if c in need:
                window[c] = window.get(c, 0) + 1

        l, r = 0, len(s1) - 1
        while r < len(s2):
            # print(f"window:{window}")
            if need == window:
                return True
            else:
                if s2[l] in need:
                    window[s2[l]] -= 1
                l += 1
                r += 1
                if r < len(s2) and s2[r] in need:
                    window[s2[r]] = window.get(s2[r], 0) + 1
            # print(f"l:{l}; r:{r}")
        return False

        