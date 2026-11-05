class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_occurance_s = [0]*26
        char_occurance_t = [0]*26
        for i in s:
            char_occurance_s[ord(i) - 97] += 1

        for i in t:
           char_occurance_t[ord(i) - 97] += 1
        
        for i in range(0,26):
            if char_occurance_s[i] != char_occurance_t[i]:
                return False
        return True
        