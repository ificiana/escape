import arcade
from pyglet.math import Vec2

from assets import sprites


class Entity(arcade.Sprite):
    def __init__(self, sprite_file):
        super().__init__()
        self.cur_texture = 0
        self.scale = 1  # defaults to 1
        self.idle_texture = arcade.load_texture(sprites.resolve(sprite_file))
        self.texture = self.idle_texture
        self.set_hit_box(self.texture.hit_box_points)

    def get_position(self):
        return Vec2(self.center_x, self.center_y)
