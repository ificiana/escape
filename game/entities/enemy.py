import random

import arcade
from pyglet.math import Vec2
from game.entities import Entity


class Enemy(Entity):
    def __init__(self, initial_pos, game_view, barriers, arrows):
        super().__init__("enemy.png")
        self.speed = 1.8
        self.health = 100
        self.game_view = game_view
        self.position = initial_pos
        self.rng = random.Random(f"{str(self.position)}1")
        self.arrows = arrows
        self.barriers = arcade.SpriteList(barriers)
        self.is_inside_view = True
        self.movement = Vec2(0, 0)
        self.is_chasing = False
        self.init_pos = initial_pos

        if overlap := self.collides_with_list(self.arrows):
            match overlap[0].properties["dir"]:
                case "up":
                    self.movement = Vec2(0, 1)
                case "down":
                    self.movement = Vec2(0, -1)
                case "left":
                    self.movement = Vec2(-1, 0)
                case "right":
                    self.movement = Vec2(1, 0)

    def move(self):
        if not self.is_inside_view:
            return
        pos = Vec2(*self.position)
        self.position = pos + self.movement * Vec2(self.speed, self.speed)

        # # TODO: remove from final, for debug
        # for barrier in self.barriers:
        #     if self.collides_with_list(barrier):
        #         print("hitting walls, fixme", self.position)

    def is_close_to_player(self, player_position: Vec2):
        distance = player_position - self.get_position()
        return distance.mag <= 100 * self.speed

    def chase_player(self, player_position: Vec2):
        self.is_chasing = True
        self.movement = (player_position - self.get_position()).normalize()

    def back_to_patrolling(self):
        if not self.is_chasing:
            return
        if self.get_position() != self.init_pos:
            self.movement = (Vec2(*self.init_pos) - self.get_position()).normalize()
        else:
            self.is_chasing = False
            if overlap := self.collides_with_list(self.arrows):
                match overlap[0].properties["dir"]:
                    case "up":
                        self.movement = Vec2(0, 1)
                    case "down":
                        self.movement = Vec2(0, -1)
                    case "left":
                        self.movement = Vec2(-1, 0)
                    case "right":
                        self.movement = Vec2(1, 0)

    def take_damage(
        self,
        amount: int = 20,
    ):
        self.health -= amount
        print(self.health)
        if self.health <= 0:
            print("DEATH")
            self.kill()

    def update(self):
        campos = self.game_view.scene_camera.position
        offset = Vec2(
            self.game_view.window.width / 1.8, self.game_view.window.height / 1.8
        )
        self.is_inside_view = (
            campos.x + self.game_view.window.width / 2 + offset.x
            >= self.center_x
            >= campos.x + self.game_view.window.width / 2 - offset.x
            and campos.y + self.game_view.window.height / 2 + offset.y
            >= self.center_y
            >= campos.y + self.game_view.window.height / 2 - offset.y
        )

        if not self.is_inside_view:
            return

        if not self.is_chasing:
            if overlap := self.collides_with_list(self.arrows):
                match overlap[0].properties["dir"]:
                    case "up":
                        self.movement = Vec2(0, 1)
                    case "down":
                        self.movement = Vec2(0, -1)
                    case "left":
                        self.movement = Vec2(-1, 0)
                    case "right":
                        self.movement = Vec2(1, 0)

        if self.health <= 0:
            print("DEATH")
            # Decrement counter for the number of enemies that touched the player when enemy dies
            self.game_view.player.num_touching_player = max(
                0, self.game_view.player.num_touching_player - 1
            )
            self.kill()

        # Call the `move` method to move the enemy
        self.move()
