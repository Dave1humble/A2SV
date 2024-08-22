class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
     
        left = 0
        s1counter = Counter(s1)
        s2counter = Counter(s2[:len(s1)-1])
        for right in range(len(s1)-1, len(s2)):
            s2counter[s2[right]] += 1

            if s2counter == s1counter:
                return True
            else:
                s2counter[s2[left]] -= 1
                if s2counter[s2[left]] == 0:
                    del s2counter[s2[left]] 
                left += 1
        return False
       
        
