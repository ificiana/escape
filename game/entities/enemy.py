from pyglet.math import Vec2

from game.entities import Entity


class Enemy(Entity):
    def __init__(self, player, game_view):
        super().__init__("enemy.png")
        self.angle = -90
        self.speed = 3.0
        self.player = player
        self.health = 100
        self.game_view = game_view
        self.center_x, self.center_y = Vec2(300, 900)
        self.state = "patrolling"

    def take_damage(
        self,
        amount: int = 20,
    ):
        self.health -= amount
        print(self.health)
        if self.health <= 0:
            print("DEATH")
            self.kill()
            # self.game_view.remove_enemy_from_world(self)

    def update(self):
        pass
        # if self.state == "patrolling":
        #     # Patrolling
        #     point = self.patrol_path[self.patrol_path_index]
        #     direction = Vec2(point[0], point[1]) - self.get_position()
        #     if direction.mag < 5:
        #         self.patrol_path_index += 1 if self.moving_forward else -1
        #         if self.patrol_path_index == len(self.patrol_path) - 1:
        #             self.moving_forward = False
        #         elif self.patrol_path_index == 0:
        #             self.moving_forward = True
        # elif self.state == "chasing":
        #     # Calculate direction to the player
        #     direction = self.player.get_position() - self.get_position()
        # if direction.mag != 0:
        #     direction = direction.normalize()
        #     self.angle = math.degrees(direction.heading)
        # # Move towards the player
        # self.center_x += direction.x * self.speed
        # self.center_y += direction.y * self.speed
