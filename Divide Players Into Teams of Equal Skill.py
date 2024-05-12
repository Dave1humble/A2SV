class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        orderd = sorted(skill) 
        count = 0
        left, right = 1, len(skill) - 2
        target = orderd[0] + orderd[-1]
        while left <= right:
            if orderd[left] + orderd[right] == target:
                count+= (orderd[left])* (orderd[right])
                left+=1
                right-=1
                
            else:
                return -1
        return count +(orderd[0] * orderd[-1])

            
            
          


        
