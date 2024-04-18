class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)  
        n = len(s)
        l = 0
        r = n-1
        while l <= r:
            if s[l] in vowels and s[r] in vowels:
            
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l +=1
                r -=1
            elif s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
        return ''.join(s)  
