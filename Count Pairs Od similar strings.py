class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def is_similar(w1, w2):
            return set(w1) == set(w2)
        
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(words[i], words[j]):
                    count += 1
        
        return count
