import random
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
        self.barriers = barriers
        self.is_inside_view = True
        self.movement = Vec2(0, 0)

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

    def move(self, reverse=False):
        if not self.is_inside_view:
            return
        n = Vec2(-1, -1) if reverse else Vec2(1, 1)
        pos = Vec2(*self.position)
        self.position = pos + n * self.movement * Vec2(self.speed, self.speed)

        # TODO: remove from final, for debug
        for barrier in self.barriers:
            if self.collides_with_list(barrier):
                print("hitting walls, fixme", self.position)

    def take_damage(
        self,
        amount: int = 20,
    ):
        self.health -= amount
        print(self.health)
        if self.health <= 0:
            print("DEATH")
            self.game_view.remove_enemy_from_world(self)

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

        self.move()
