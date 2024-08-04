class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = sorted(points)
        max_width = 0
        for i in range(len(ans)-1):
            difference = ans[i+1][0] - ans[i][0]
            max_width = max(max_width, difference)

        return max_width

        
