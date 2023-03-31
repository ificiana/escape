import math

from pyglet.math import Vec2

from game.entities import Entity


class Player(Entity):
    def __init__(self, game_view):
        super().__init__("mc_idle.png")
        self.center_x, self.center_y = Vec2(0, 0)
        self.angle = -90
        self.normal_speed = 2.0
        self.speed = self.normal_speed
        self.game_view = game_view

    def update_animation(self, delta_time: float = 1 / 60):
        pass

    def move(self, delta_pos: Vec2, mouse_pos: Vec2):
        direction = mouse_pos - self.get_position()
        if direction.mag != 0:
            direction = direction.normalize()
            self.angle = math.degrees(direction.heading)
        self.center_x += delta_pos.x * self.speed
        self.center_y += delta_pos.y * self.speed

    def update_player(self):
        nearest_item, nearest_dist = None, 99999
        for item in self.game_view.pickables:
            distance = self.get_position() - item.get_position()
            if distance.mag < nearest_dist:
                nearest_dist = distance.mag
                nearest_item = item
        if nearest_item is not None and nearest_dist < 64:
            self.game_view.set_display_text("Press H to pick up")
        else:
            self.game_view.set_display_text("")

    def attack(self):
        nearest_enemy, nearest_dist = None, 99999
        for entity in self.game_view.entities_list:
            if entity == self:
                continue
            distance = self.get_position() - entity.get_position()
            if distance.mag < nearest_dist:
                nearest_dist = distance.mag
                nearest_enemy = entity
        if nearest_enemy is not None and nearest_dist < 64 * 1.5:
            # TODO: Play attack animation
            nearest_enemy.take_damage(25)

    def change_speed(self, slow_factor: float = 0.25):
        """1.0 for normal speed and 0.0 for complete stop"""
        self.speed = self.normal_speed * slow_factor
