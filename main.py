import pygame
from pygame.locals import *
from generator import Walker, Grid
from utils import Vector2

pygame.init()


class Maze:
    def __init__(self, grid_size: Vector2, cell_size: Vector2):
        self.grid = Grid(grid_size)
        walker = Walker(self.grid)
        walker.walk()
        self.grid = walker.grid

        self.cell_size = cell_size
        self.window = pygame.display.get_surface()

    def update(self):
        for key in list(self.grid.array.keys()):
            position = key.split(";")
            x, y = int(position[0]), int(position[1])

            cell = self.grid.array[key]

            start_pos = Vector2(self.cell_size.X * x, self.cell_size.Y * y)
            end_pos = start_pos + Vector2(self.cell_size.X, 0)

            if "top" in cell.walls:
                pygame.draw.line(self.window, (255, 255, 255), start_pos.position, end_pos.position)

            if "right" in cell.walls:
                start_pos += Vector2(self.cell_size.X, 0)
                end_pos += Vector2(0, -self.cell_size.Y)

                pygame.draw.line(self.window, (255, 255, 255), start_pos.position, end_pos.position)


def main():
    window = pygame.display.set_mode((800, 600), RESIZABLE)
    clock = pygame.time.Clock()

    maze = Maze(Vector2(16, 16), Vector2(32, 32))

    brake = False
    while not brake:
        for event in pygame.event.get():
            if event.type == QUIT:
                brake = True

        maze.update()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
