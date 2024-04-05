class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = []
        if not words:
            return c
        
        f = {}
        
        for char in words[0]:
            count = words[0].count(char)
            f[char] = count
        
        for word in words[1:]:
            tf = {}
            for char in word:
                if char in f:
                    count = word.count(char)
                    tf[char] = count
            
            for char in f:
                if char not in tf:
                    f[char] = 0
                else:
                    f[char] = min(f[char], tf[char])
        
        for char, frequency in f.items():
            c.extend([char] * frequency)
        
        return c
