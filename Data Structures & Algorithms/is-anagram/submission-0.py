class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = {}
        c_t = {}

        for c in s:
            if c not in c_s:
                c_s[c] = 0
            c_s[c] = c_s[c] + 1
        for c in t:
            if c not in c_t:
                c_t[c] = 0
            c_t[c] = c_t[c] + 1
        
        for c in c_s:
            if c not in c_t or c_s[c] != c_t[c]:
                return False

        for c in c_t:
            if c not in c_s or c_s[c] != c_t[c]:
                return False
        
        return True