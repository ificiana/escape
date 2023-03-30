import math

from pyglet.math import Vec2

from game.config import SCREEN_WIDTH, SCREEN_HEIGHT
from game.entities import Entity


class Player(Entity):
    def __init__(self):
        super().__init__("mc_idle.png")
        self.center_x, self.center_y = Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.angle = -90
        self.speed = 4.0

    def update_animation(self, delta_time: float = 1 / 60):
        pass

    def move(self, dx, dy, mouse_x, mouse_y):
        direction = Vec2(mouse_x, mouse_y) - Vec2(self.center_x, self.center_y)
        if direction.mag != 0:
            direction = direction.normalize()
            self.angle = math.degrees(direction.heading)
        self.center_x += dx * self.speed
        self.center_y += dy * self.speed
