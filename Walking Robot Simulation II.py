class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = 2 * (width + height) - 4
        self.position = 0  # starting position
        self.directions = ["East", "North", "West", "South"]
        self.current_dir = "East"
        self.x = 0
        self.y = 0

    def step(self, num: int) -> None:
        num = num % self.perimeter
        while num > 0:
            if self.current_dir == "East":
                move = min(num, self.width - 1 - self.x)
                self.x += move
                num -= move
                if self.x == self.width - 1 and num > 0:
                    self.current_dir = "North"
            elif self.current_dir == "North":
                move = min(num, self.height - 1 - self.y)
                self.y += move
                num -= move
                if self.y == self.height - 1 and num > 0:
                    self.current_dir = "West"
            elif self.current_dir == "West":
                move = min(num, self.x)
                self.x -= move
                num -= move
                if self.x == 0 and num > 0:
                    self.current_dir = "South"
            elif self.current_dir == "South":
                move = min(num, self.y)
                self.y -= move
                num -= move
                if self.y == 0 and num > 0:
                    self.current_dir = "East"
        if self.x == 0 and self.y == 0:
            self.current_dir = "South"

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.current_dir

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
