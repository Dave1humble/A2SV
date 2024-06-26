class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res=[]
        left, right = 0, 0
        while left < len(word1) and right < len(word2):
            if word1[left:] > word2[right:]:
                res.append(word1[left])
                left+=1
            else:
                res.append(word2[right])
                right+=1
        res.append(word1[left:])
        res.append(word2[right:])
        return ''.join(res)
