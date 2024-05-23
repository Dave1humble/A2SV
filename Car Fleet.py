class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted([(position[i], (target - position[i]) / speed[i]) for i in range(n)], reverse=True)
        fleets = 0
        prev_time = -1
        
        for _, time in cars:
            if time > prev_time:
                fleets += 1
                prev_time = time
                
        return fleets
