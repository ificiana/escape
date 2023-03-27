import math

import arcade
from pyglet.math import Vec2

from assets import sprites

from .config import *

MC_SCALE = 0.4


class Entity(arcade.Sprite):
    def __init__(self, sprite_file):
        super().__init__()
        self.cur_texture = 0
        self.scale = MC_SCALE
        self.idle_texture = arcade.load_texture(sprites.resolve(sprite_file))
        # self.walk_textures = []
        # for i in range(8):
        #     texture = arcade.load_texture(f"{main_path}_walk{i}.png")
        #     self.walk_textures.append(texture)
        self.texture = self.idle_texture
        self.set_hit_box(self.texture.hit_box_points)


class MC(Entity):
    def __init__(self):
        super().__init__("mc_idle.png")
        self.center_x, self.center_y = Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.angle = -90
        self.speed = 4.0

    def update_animation(self, delta_time: float = 1 / 60):
        pass
        # # Idle animation
        # if self.change_x == 0 and self.change_y == 0:
        #     self.texture = self.idle_texture
        #     return
        # # Walking animation
        # self.cur_texture += 1
        # if self.cur_texture > 7:
        #     self.cur_texture = 0
        # self.texture = self.walk_textures[self.cur_texture]

    def move(self, dx, dy, mouse_x, mouse_y):
        direction = Vec2(mouse_x, mouse_y) - Vec2(self.center_x, self.center_y)
        if direction.mag != 0:
            direction = direction.normalize()
            self.angle = math.degrees(direction.heading)
        self.center_x += dx * self.speed
        self.center_y += dy * self.speed

    def show(self):
        self.draw()

    def get_position(self):
        return Vec2(self.center_x, self.center_y)
