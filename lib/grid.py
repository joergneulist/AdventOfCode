
class CharGrid:
    def __init__(self, grid):
        self.grid = grid
        self.shape = (len(self.grid[0]), len(self.grid))

    def __str__(self):
        return '\n'.join(self.grid)

    def __getitem__(self, coords):
        return self.getc(coords)

    def __setitem__(self, coords, value):
        self.setc(coords, value)

    def walk(self):
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                yield x, y

    def getc(self, coords):
        if coords is not None:
            x, y = coords
            if x >= 0 and y >= 0 and y < self.shape[1] and x < self.shape[0]:
                return self.grid[y][x]

    def setc(self, coords, new):
        if coords is not None:
            x, y = coords
            if x >= 0 and y >= 0 and y < self.shape[1] and x < self.shape[0]:
                self.grid[y] = self.grid[y][:x] + new + self.grid[y][x+1:]

    def up(self, coords):
        x, y = coords
        return x, y - 1

    def down(self, coords):
        x, y = coords
        return x, y + 1

    def left(self, coords):
        x, y = coords
        return x - 1, y

    def right(self, coords):
        x, y = coords
        return x + 1, y

    def neighbours(self, coords):
        return self.up(coords), self.down(coords), self.left(coords), self.right(coords)
