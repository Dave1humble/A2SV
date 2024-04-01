class Solution:
    def freqAlphabets(self, s: str) -> str:
        small_alphabets = ' abcdefghijklmnopqrstuvwxyz'
        mapp = {}
        n = len(s)
        for i in range(1, 27):
            if i<=9:
                mapp[str(i)] = small_alphabets[i]
            else:
                mapp[str(i) + "#"] = small_alphabets[i]
        res = ''
        i = 0
        while i < n: 
            if i + 2 < n and s[i+2] == "#":
                res += mapp[s[i:i+3]]
                i += 3
            else:
                res += mapp[s[i]]
                i += 1
        return res
