import math
import arcade

from pyglet.math import Vec2

from game.config import SCREEN_WIDTH, SCREEN_HEIGHT
from game.entities import Entity


class Player(Entity):
    def __init__(self):
        super().__init__("mc_idle.png")
        self.center_x, self.center_y = Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.angle = -90
        self.normal_speed = 4.0
        self.speed = self.normal_speed

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

    def move(self, delta_pos: Vec2, mouse_pos: Vec2):
        direction = mouse_pos - self.get_position()
        if direction.mag != 0:
            direction = direction.normalize()
            self.angle = math.degrees(direction.heading)
        self.center_x += delta_pos.x * self.speed
        self.center_y += delta_pos.y * self.speed

    def attack(self, entities_list: arcade.SpriteList):
        nearest_enemy, nearest_dist = None, 99999
        for entity in entities_list:
            distance = self.get_position() - entity.get_position()
            if distance.mag < nearest_dist:
                nearest_dist = distance.mag
                nearest_enemy = entity
        if nearest_enemy != None:
            # TODO: Play attack animation
            nearest_enemy.take_damage(25)      # In Enemy class implement take_damage() function

    def change_speed(self, slow_factor: float = 0.25):
        """1.0 for normal speed and 0.0 for complete stop"""
        self.speed = self.normal_speed * slow_factor

    def show(self):
        self.draw()

    def get_position(self):
        return Vec2(self.center_x, self.center_y)
