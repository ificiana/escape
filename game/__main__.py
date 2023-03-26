import arcade
from pyglet.math import clamp, Vec2

import assets

from .config import *
from .entities import MC

# pylint: disable=global-statement
# TODO: fix this

Xinput, Yinput = 0, 0
mouseX, mouseY = 0, 0
worldMouseX, worldMouseY = mouseX, mouseY


def placeWalls():
    walls = arcade.SpriteList()
    rect = [100, 100, 64 * 10, 64 * 10]  # Placing walls around this rect
    for i in range(rect[0], rect[0] + rect[2] + 64, 64):
        wall = arcade.Sprite(
            assets.sprites.resolve("wall.png"), center_x=i, center_y=rect[1]
        )
        walls.append(wall)
        wall = arcade.Sprite(
            assets.sprites.resolve("wall.png"), center_x=i, center_y=rect[1] + rect[3]
        )
        walls.append(wall)
    for j in range(rect[1], rect[1] + rect[3], 64):
        wall = arcade.Sprite(
            assets.sprites.resolve("wall.png"), center_x=rect[0], center_y=j
        )
        walls.append(wall)
        wall = arcade.Sprite(
            assets.sprites.resolve("wall.png"), center_x=rect[0] + rect[2], center_y=j
        )
        walls.append(wall)
    return walls


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.mc = MC()
        self.walls = placeWalls()
        self.sceneCamera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.mc, self.walls
        )  # Create physics engine for collision

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        global worldMouseX, worldMouseY
        worldMouseX, worldMouseY = (
            mouseX + self.sceneCamera.position.x,
            mouseY + self.sceneCamera.position.y,
        )
        self.mc.move(Xinput, Yinput, worldMouseX, worldMouseY)
        self.physics_engine.update()
        # Collision is Glitchy

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((50, 50, 50))
        self.sceneCamera.use()
        camPos = Vec2(
            self.mc.pos.x - SCREEN_WIDTH / 2, self.mc.pos.y - SCREEN_HEIGHT / 2
        )
        self.sceneCamera.move_to(camPos)
        self.mc.draw()
        self.walls.draw()

    # Handle Keyboard Input
    # Navigate with WASD or Arrow keys and use Mouse for direction
    def on_key_press(self, symbol: int, modifiers: int):
        global Xinput, Yinput
        if symbol in [arcade.key.DOWN, arcade.key.S]:
            Yinput = -1
        if symbol in [arcade.key.UP, arcade.key.W]:
            Yinput = 1
        if symbol in [arcade.key.LEFT, arcade.key.A]:
            Xinput = -1
        if symbol in [arcade.key.RIGHT, arcade.key.D]:
            Xinput = 1
        Xinput = clamp(Xinput, -1, 1)

    def on_key_release(self, symbol: int, modifiers: int):
        global Xinput, Yinput
        if symbol in [arcade.key.DOWN, arcade.key.S]:
            Yinput = 0
        if symbol in [arcade.key.UP, arcade.key.W]:
            Yinput = 0
        if symbol in [arcade.key.LEFT, arcade.key.A]:
            Xinput = 0
        if symbol in [arcade.key.RIGHT, arcade.key.D]:
            Xinput = 0
        Xinput = clamp(Xinput, -1, 1)

    # Handle Mouse Events
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        global mouseX, mouseY, worldMouseX, worldMouseY
        mouseX, mouseY = x, y
        worldMouseX, worldMouseY = (
            mouseX + self.sceneCamera.position.x,
            mouseY + self.sceneCamera.position.y,
        )


def main():
    Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Mental Asylum")
    arcade.run()
