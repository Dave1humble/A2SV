class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words.sort(key=lambda word: word[-1])
        sorted_words = []
        for word in words:
            sorted_words.append(word[:-1])
        
        sorted_sentence = ' '.join(sorted_words)
        return sorted_sentence
