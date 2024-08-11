class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        maxx = max(skill)
        res = [0] * (maxx + 1)
        for skil in skill:
            res[skil] += 1
        i = 0
        for c in range(maxx + 1):
            while res[c] > 0:
                skill[i] = c
                i += 1
                res[c] -= 1
        left = 0
        right = n - 1
        summ = 0
        target = skill[left] + skill[right]
       
        while left < right:
            if skill[left] + skill[right] == target:
                summ += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        
        return summ



    


        



        

            
            
          


        
