class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        res = 0
        k = int(n/3)
        for i in range(k,n,2):
            res += piles[i]
            

        return res   
        
