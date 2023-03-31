import math

import arcade
from pyglet.math import Vec2

from game.entities import Entity


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
                if self.patrol_path_index == len(self.patrol_path) - 1:
                    self.moving_forward = False
                elif self.patrol_path_index == 0:
                    self.moving_forward = True
        elif self.state == "chasing":
            # Calculate direction to the player
            direction = self.player.get_position() - self.get_position()
        if direction.mag != 0:
            direction = direction.normalize()
            self.angle = math.degrees(direction.heading)
        # Move towards the player
        self.center_x += direction.x * self.speed
        self.center_y += direction.y * self.speed
