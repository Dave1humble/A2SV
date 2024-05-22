class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l = 0
        counts = [0] * 26
        n = len(s)
        for r in range(n):
            counts[ord(s[r]) - 65] += 1
            while (r-l+1) - max(counts) >k:
                counts[ord(s[l])-65] -= 1
                l+=1
            max_length = max(max_length, (r-l+1))
        return max_length
