class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        maximum = 0
        for i, c in enumerate(s):
            if c in seen:
                index = seen[c]
                for j in range(l, index + 1):
                    seen.pop(s[j])
                l = index + 1
            seen[c] = i
            maximum = max(maximum, i - l + 1)
            # print(c, seen)
        return maximum