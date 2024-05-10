class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0  
        ordered = sorted(people)  

        left = 0
        right = len(ordered) - 1

        while left <= right:
            if ordered[left] + ordered[right] <= limit:
                boats += 1  
                left += 1
                right -= 1
            else: 
                right -= 1
                boats += 1 
        return boats
