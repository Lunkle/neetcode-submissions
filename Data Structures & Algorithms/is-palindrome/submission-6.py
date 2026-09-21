class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabet = list("abcdefghijklmnopqrstuvwxyz") + list("0123456789")
        new_s = ""
        for c in s:
            if c in alphabet:
                new_s += c
        s = new_s
        print(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True