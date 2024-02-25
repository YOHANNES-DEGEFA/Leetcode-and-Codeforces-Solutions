class Robot:
    def __init__(self, width: int, height: int):
        self.direction = "East"
        self.coordinates = [0, 0]
        self.target_coordinates = [width - 1, height - 1]
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        total_steps = (self.height + self.width - 2) * 2
        num = num % total_steps

        if num != 0:
            i = 0
            while i < num:
                if self.direction == "East":
                    if self.coordinates[0] == self.width - 1:
                        num += 1
                        self.direction = "North"
                    else:
                        self.coordinates[0] += 1
                elif self.direction == "West":
                    if self.coordinates[0] == 0:
                        num += 1
                        self.direction = "South"
                    else:
                        self.coordinates[0] -= 1
                elif self.direction == "North":
                    if self.coordinates[1] == self.height - 1:
                        num += 1
                        self.direction = "West"
                    else:
                        self.coordinates[1] += 1
                elif self.direction == "South":
                    if self.coordinates[1] == 0:
                        num += 1
                        self.direction = "East"
                    else:
                        self.coordinates[1] -= 1
                i += 1
        elif self.coordinates == [0, 0] and self.direction == "East":
            self.direction = "South"

    def getPos(self) -> List[int]:
        return self.coordinates

    def getDir(self) -> str:
        return self.direction