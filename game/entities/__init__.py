import arcade
from pyglet.math import Vec2

from assets import sprites


class Entity(arcade.Sprite):
    def __init__(self, sprite_file):
        super().__init__()
        self.cur_texture = 0
        self.scale = 0.4  # defaults to 0.4
        self.idle_texture = arcade.load_texture(sprites.resolve(sprite_file))
        # self.walk_textures = []
        # for i in range(8):
        #     texture = arcade.load_texture(f"{main_path}_walk{i}.png")
        #     self.walk_textures.append(texture)
        self.texture = self.idle_texture
        self.set_hit_box(self.texture.hit_box_points)

    def get_position(self):
        return Vec2(self.center_x, self.center_y)
