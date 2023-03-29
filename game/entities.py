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
    def get_position(self):
        return Vec2(self.center_x, self.center_y)


class Player(Entity):
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


class Enemy(Entity):
    def __init__(self, player, barrier_list):
        super().__init__("slimeBlock.png")
        self.angle = -90
        self.speed = 3.0
        self.player = player
        self.barrier_list = barrier_list
        start = Vec2(300, 900)
        end = Vec2(1200, 1280)
        self.patrol_path = self.calculate_path(start, end)
        self.patrol_path_index = 0
        self.center_x, self.center_y = self.patrol_path[self.patrol_path_index]
        self.state = "patrolling"
        self.moving_forward = True

    def calculate_path(self, start, end):
        return arcade.astar_calculate_path(start, end, self.barrier_list, True)
        
    def update(self):
        if self.state == "patrolling":
            # Patrolling
            point = self.patrol_path[self.patrol_path_index]
            direction = Vec2(point[0], point[1]) - self.get_position()
            if direction.mag < 5:
                self.patrol_path_index += 1 if self.moving_forward else -1
                if self.patrol_path_index == len(self.patrol_path)-1: self.moving_forward = False
                elif self.patrol_path_index == 0: self.moving_forward = True
        elif self.state == "chasing":
            # Calculate direction to the player
            direction = self.player.get_position() - self.get_position()
        if direction.mag != 0:
            direction = direction.normalize()
            self.angle = math.degrees(direction.heading)
        # Move towards the player
        self.center_x += direction.x * self.speed
        self.center_y += direction.y * self.speed

    def show(self):
        self.draw()
