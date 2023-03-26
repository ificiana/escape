import arcade
import math
import pygame
from config import *

MC_SCALE = 0.4

class Entity(arcade.Sprite):
    def __init__(self, name_folder, name_file):
        super().__init__()
        self.cur_texture = 0
        self.scale = MC_SCALE
        main_path = f"{name_folder}/{name_file}"
        self.idle_texture = arcade.load_texture(f"{main_path}_idle.png")
        # self.walk_textures = []
        # for i in range(8):
        #     texture = arcade.load_texture(f"{main_path}_walk{i}.png")
        #     self.walk_textures.append(texture)
        self.texture = self.idle_texture
        self.set_hit_box(self.texture.hit_box_points)

class MC(Entity):
    def __init__(self):
        super().__init__("sprites", "mc")
        self.pos = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.angle = -90
        self.speed = 6.0
    def update_animation(self, dt: float = 1 / 60):
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
    def move(self, dx, dy, mouseX, mouseY):
        self.pos += pygame.Vector2(dx, dy)
        direction = pygame.Vector2(mouseX, mouseY) - self.pos
        if direction.length() != 0:
            direction = direction.normalize()
            self.angle = math.degrees(math.atan2(direction.y, direction.x))
        self.center_x = self.pos.x
        self.center_y = self.pos.y
    def show(self):
        self.draw()
        