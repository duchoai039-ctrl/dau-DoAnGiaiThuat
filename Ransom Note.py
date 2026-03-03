class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}

        for i in magazine:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1

        for c in ransomNote:
            if c not in letters:
                return False
            elif letters[c] == 1:
                del letters[c]
            else:
                letters[c] -= 1 

        return True
        