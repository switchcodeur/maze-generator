from random import choice as rchoice
from utils import Vector2


class Cell:
    def __init__(self):
        self.visited = False
        self.walls = ["top", "right"]

    def remove_wall(self, wall: str):
        if wall in self.walls:
            self.walls.remove(wall)


class Grid:
    def __init__(self, size: Vector2):
        self.size = size
        self.array = {}

        for y in range(size.Y):
            for x in range(size.X):
                self.array[f"{x};{y}"] = Cell()

    def has_been_visited(self, position: Vector2):
        if any([
            position.X < 0,
            position.X >= self.size.X,
            position.Y < 0,
            position.Y >= self.size.Y
        ]):
            return True

        return self.array[f"{position.X};{position.Y}"].visited or position

    def remove_wall(self, start: Vector2, end: Vector2):
        move = end - start
        
        if move.position == (0, 1):
            self.array[f"{end.X};{end.Y}"].remove_wall("top")
        elif move.position == (0, -1):
            self.array[f"{start.X};{start.Y}"].remove_wall("top")
        elif move.position == (1, 0):
            self.array[f"{start.X};{start.Y}"].remove_wall("right")
        elif move.position == (-1, 0):
            self.array[f"{end.X};{end.Y}"].remove_wall("right")


class Walker:
    def __init__(self, grid: Grid):
        self.position = Vector2(0, 0)
        self.path = [self.position]
        self.grid = grid

    def get_possibles_moves(self):
        possibilities = []

        for attempt in [
            self.grid.has_been_visited(self.position + Vector2(0, 1)),
            self.grid.has_been_visited(self.position + Vector2(0, -1)),
            self.grid.has_been_visited(self.position + Vector2(1, 0)),
            self.grid.has_been_visited(self.position + Vector2(-1, 0))
        ]:
            if isinstance(attempt, Vector2):
                possibilities.append(attempt)

        return possibilities

    def move_forward(self, possibilities: list):
        choice = rchoice(possibilities)

        self.grid.remove_wall(self.position, choice)
        self.grid.array[f"{choice.X};{choice.Y}"].visited = True

        self.path.append(choice)
        self.position = choice

    def move_backward(self):
        self.position = self.path[-1]
        self.path.pop(-1)

    def walk(self):
        possibilities = self.get_possibles_moves()

        self.move_forward(possibilities) if possibilities \
            else self.move_backward()
