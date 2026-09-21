class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {} # nunm : (seq start, seq end)

        for i in nums:
            if i in m:
                continue
            if i + 1 in m and i - 1 in m:
                m[i] = [0, 0]
                m[i + m[i + 1][0]][1] += 1 + m[i - 1][1]
                m[i - m[i - 1][1]][0] += 1 + m[i + 1][0]
                m[i + 1][0] = 0
                m[i - 1][1] = 0
            elif i + 1 in m:
                m[i] = [1 + m[i + 1][0], 0]
                m[i + m[i + 1][0]][1] += 1
                m[i + 1][0] = 0
            elif i - 1 in m:
                m[i] = [0, 1 + m[i - 1][1]]
                m[i - m[i - 1][1]][0] += 1
                m[i - 1][1] = 0
            else:
                m[i] = [1, 1]

        maximum = 0
        for i, j in m.values():
            maximum = max(maximum, i)
        return maximum