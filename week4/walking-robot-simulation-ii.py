class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.next_dir = {
            'East': 'North',
            'North': 'West',
            'West': 'South',
            'South': 'East'
        }
        self.moves = {
            'East': [1, 0],
            'North': [0, 1],
            'West': [-1, 0],
            'South': [0, -1]
        }

        self.current_position = [0, 0]
        self.direction = 'East'

        self.full_loop = self.width * 2 + self.height * 2

    def step(self, num: int) -> None:

        if num > self.full_loop:
            num = num - (num // self.full_loop) * self.full_loop

            if num == 0 and self.current_position == [0, 0]:
                self.direction = 'South'

        while num > 0:
            cur_move = self.moves[self.direction]
            max_move = min(self.max_move_dir(), num)
            num -= max_move
            new_width, new_height = self.current_position[0] + cur_move[0] * max_move, self.current_position[1] + cur_move[1] * max_move
            self.current_position = [new_width, new_height]
            if num > 0:
                self.direction = self.next_dir[self.direction]
                
    def max_move_dir(self):
        if self.direction == 'East':
            return self.width - self.current_position[0]
        if self.direction == 'North':
            return self.height - self.current_position[1]
        if self.direction == 'West':
            return self.current_position[0] - 0
        if self.direction == 'South':
            return self.current_position[1] - 0

    def getPos(self) -> List[int]:
        return self.current_position

    def getDir(self) -> str:
        return self.direction


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()