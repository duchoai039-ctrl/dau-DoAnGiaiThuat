class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        for c, i in enumerate(s):
            if d[i] == 1:
                return c
        return  -1
        