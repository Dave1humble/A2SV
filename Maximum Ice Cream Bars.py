class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        maxx = max(costs)
        res = [0] * (maxx + 1)
        
        for cost in costs:
            res[cost] += 1

        i = 0
        for c in range(maxx + 1):
            while res[c] > 0:
                costs[i] = c
                i += 1
                res[c] -= 1
      
        summ = 0
        count = 0
        for i in range(n):
            if summ + costs[i] <= coins:
                summ += costs[i]
                count += 1
            else:
                break
        
        return count
