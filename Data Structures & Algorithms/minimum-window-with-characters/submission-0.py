class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)
        l = 0
        res, min_length = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < min_length:
                    res = [l, r]
                    min_length = (r - l + 1)

                left_c = s[l]
                window[left_c] -= 1
                if left_c in count_t and window[left_c] < count_t[left_c]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if min_length != float("infinity") else ""






        

        