class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = ''
        for i, word in enumerate(sentence.split(' ')):
            if word[0] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                new_word = word + 'ma' + 'a' * (i+1)
                ans += new_word
            else:
                new_word = word[1:] + word[0] + 'ma' + 'a' * (i+1)
                ans += new_word
            ans += ' '
        return ans.strip()