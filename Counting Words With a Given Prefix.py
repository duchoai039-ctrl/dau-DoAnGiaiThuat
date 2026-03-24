class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        dem = 0
        for i in words:
            if i.startswith(pref): #ham co san chu do co bat dau bang tien to ko
                dem+=1
        return dem

        