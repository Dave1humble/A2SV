import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.isqrt(c))
        while l <= r :
            current_sum = l*l + r*r
            if current_sum == c:
                return True
            elif current_sum < c:
                l+=1
            elif current_sum> c:
                r-=1
        return False
