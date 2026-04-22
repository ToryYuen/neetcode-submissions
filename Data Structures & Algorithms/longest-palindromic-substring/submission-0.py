class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_l = ans_r = max_len = 0

        for center in range(len(s)):
            l = r = center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = (r - l + 1)
                    ans_l = l
                    ans_r = r
                l -= 1
                r += 1
            
            l, r = center, center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = (r - l + 1)
                    ans_l = l
                    ans_r = r
                l -= 1
                r += 1

        return s[ans_l:ans_r + 1]
        