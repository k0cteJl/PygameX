import pygame

from ..Object import Object


class Player(Object):

    def __init__(self, position: tuple = (0, 0), size: tuple = (50, 50), color: tuple = (255, 255, 255), thickness: int = 0, position_limits: tuple = None):
        self.position = position
        self.size = size
        self.color = color
        self.thickness = thickness
        self.position_limits = position_limits # (left x, right x, top y, bottom y)

    def render(self, screen):
        if self.thickness == 0:
            pygame.draw.rect(screen, self.color, (self.position, self.size))
        else:
            pygame.draw.rect(screen, self.color, (self.position, self.size), self.thickness)

    # (left x, right x, top y, bottom y)
    def can_move(self, x, y) -> bool:
        if self.position_limits is not None:
            return (self.position_limits[0] < (self.position[0] + x) and
                    (self.position[0] + x + self.size[0]) < self.position_limits[1] and
                    self.position_limits[2] < (self.position[1] + y) and
                    (self.position[1] + y + self.size[1]) < self.position_limits[3])
        else:
            return True

    def move(self, x, y):
        self.position = (self.position[0] + x, self.position[1] + y)

    def smart_move(self, x, y):
        xx = x
        yy = y

        if x + self.position[0] < self.position_limits[0]:
            xx = self.position_limits[0] - (x + self.position[0])
        if x + self.position[0] >= self.position_limits[1]:
            xx = (x + self.position[0]) - self.position_limits[1]

        if y + self.position[1] < self.position_limits[2]:
            yy = self.position_limits[2] - (y + self.position[1])
        if y + self.position[1] > self.position_limits[3]:
            yy = (y + self.position[1]) - self.position_limits[2]

        self.position = (self.position[0]+xx, self.position[1]+yy)

    def save_move(self, x, y):
        if self.can_move(x, 0):
            self.smart_move(x, 0)
        else:
            pass

        if self.can_move(0, y):
            self.smart_move(0, y)
        else:
            pass