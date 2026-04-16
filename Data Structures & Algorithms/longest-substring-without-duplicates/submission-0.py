class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = l = 0
        prev = {}
        for r in range(len(s)):
            if s[r] in prev:
                l = max(l, prev[s[r]] + 1)

            max_length = max(max_length, r - l + 1)
            prev[s[r]] = r
                
        return max_length