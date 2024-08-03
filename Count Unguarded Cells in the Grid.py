class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        Grid = [[0] * n for _ in range(m)]
        for guard in guards:
            Grid[guard[0]][guard[1]] = 'G'
        for wall in walls:
            Grid[wall[0]][wall[1]] = 'w'
           # Directions: right, down, left, up 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for guard in guards:
            for direction in directions:
                x, y = guard
                while True:
                    x += direction[0]
                    y += direction[1]
                    if x < 0 or x >= m or y < 0 or y >=n or Grid[x][y] in ('G', 'w'):
                        break
                    if Grid[x][y] == 0:
                        Grid[x][y] = 'x'
        unguarded = 0
        for row in range(m):
            for column in range(n):
                if Grid[row][column] == 0:
                    unguarded += 1
        return unguarded
