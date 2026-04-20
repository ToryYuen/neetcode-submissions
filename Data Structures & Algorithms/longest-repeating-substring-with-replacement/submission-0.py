class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        max_length = l = 0

        for r in range(len(s)):
            freq[ord('A') - ord(s[r])] += 1
            while (r - l + 1) - max(freq) > k:
                freq[ord('A') - ord(s[l])] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length
        