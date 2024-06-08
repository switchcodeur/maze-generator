import time

import pygame
from pygame.locals import *

from generator import Walker, Grid
from utils import Vector2

pygame.init()


class Maze:
    def __init__(self, grid_size: Vector2, cell_size: Vector2):
        self.grid = Grid(grid_size)
        self.walker = Walker(self.grid)

        self.cell_size = cell_size
        self.window = pygame.display.get_surface()

    def update(self):
        window_size = self.window.get_size()
        middle = Vector2(
            (window_size[0] - self.cell_size.X * self.grid.size.X) / 2,
            (window_size[1] - self.cell_size.Y * self.grid.size.Y) / 2
        )

        pygame.draw.line(self.window, (255, 255, 255), middle.position, (
            middle.X,
            middle.Y + self.cell_size.Y * self.grid.size.Y
        ))  # -> left wall
        pygame.draw.line(self.window, (255, 255, 255), (
            middle.X,
            middle.Y + self.cell_size.Y * self.grid.size.Y
        ), (
            middle.X + self.cell_size.X * self.grid.size.X,
            middle.Y + self.cell_size.Y * self.grid.size.Y
        ))  # -> bottom wall

        if len(self.walker.path) > 0:
            self.walker.walk()
            self.grid = self.walker.grid

        pygame.draw.rect(self.window, (0, 255, 0), (
            middle.X + self.cell_size.X * self.walker.position.X,
            middle.Y + self.cell_size.Y * self.walker.position.Y,

            self.cell_size.X,
            self.cell_size.Y
        ))  # -> walker

        for key in list(self.grid.array.keys()):
            position = key.split(";")
            position = Vector2(int(position[0]), int(position[1]))

            cell = self.grid.array[key]

            start = middle + Vector2(
                self.cell_size.X * position.X,
                self.cell_size.Y * position.Y
            )
            end = start + Vector2(
                self.cell_size.X,
                0
            )

            if "top" in cell.walls:
                pygame.draw.line(self.window, (255, 255, 255), start.position, end.position)

            if "right" in cell.walls:
                start += Vector2(self.cell_size.X, 0)
                end += Vector2(0, self.cell_size.Y)

                pygame.draw.line(self.window, (255, 255, 255), start.position, end.position)


def main():
    window = pygame.display.set_mode((800, 600), RESIZABLE)
    clock = pygame.time.Clock()

    maze = Maze(Vector2(16, 16), Vector2(32, 32))

    brake = False
    while not brake:
        for event in pygame.event.get():
            if event.type == QUIT:
                brake = True

        window.fill((0, 0, 0))
        maze.update()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
