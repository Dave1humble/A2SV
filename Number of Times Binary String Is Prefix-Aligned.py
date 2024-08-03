class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        rightmost = 0
        count = 0
        
        for i, flip in enumerate(flips):
            rightmost = max(rightmost, flip)
            if rightmost == i + 1:
                count += 1
        
        return count

        
