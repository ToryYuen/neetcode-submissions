from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2: return False

        s1_freq = [0] * 26
        window = [0] * 26
        for c in s1:
            s1_freq[ord('a') - ord(c)] += 1
        for c in s2[:n1]:
            window[ord('a') - ord(c)] += 1

        print(f"s1:{s1_freq}")
        match = 0
        for i in range(26):
            if s1_freq[i] == window[i]:
                match += 1 
        
        l = 0
        for r in range(n1, n2):
            if match == 26:
                return True
            if window[ord('a') - ord(s2[r])] == s1_freq[ord('a') - ord(s2[r])]:
                match -= 1
            if window[ord('a') - ord(s2[l])] == s1_freq[ord('a') - ord(s2[l])]:
                match -= 1

            window[ord('a') - ord(s2[r])] += 1
            window[ord('a') - ord(s2[l])] -= 1
            if window[ord('a') - ord(s2[r])] == s1_freq[ord('a') - ord(s2[r])]:
                match += 1
            if window[ord('a') - ord(s2[l])] == s1_freq[ord('a') - ord(s2[l])]:
                match += 1
            l += 1


        return match == 26
