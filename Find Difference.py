class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
       khac = Counter(t) - Counter(s)
       for i in khac:
        return i