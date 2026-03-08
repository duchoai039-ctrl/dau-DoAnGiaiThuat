class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chu = s.split()
        return(len(set(pattern)) == len(set(chu)) == len(set(zip_longest(pattern,chu))))
        
