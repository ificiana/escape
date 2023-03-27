import arcade
from pyglet.math import clamp, Vec2
from arcade.experimental.shadertoy import Shadertoy

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
        # self.walls = placeWalls()
        my_map = arcade.TileMap(assets.tilemaps.resolve("level1.tmx"), use_spatial_hash=True)
        self.walls = my_map.sprite_lists['walls']
        self.sceneCamera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.mc, self.walls
        )  # Create physics engine for collision
        # Shader related work
        self.shadertoy = None
        self.channel0 = None
        self.channel1 = None
        self.loadShader()
    
    def loadShader(self):
        shader_file_path = assets.sprites.resolve("shadow.glsl")
        window_size = self.get_size()
        self.shadertoy = Shadertoy.create_from_file(window_size, shader_file_path)
        self.channel0 = self.shadertoy.ctx.framebuffer(
            color_attachments=[self.shadertoy.ctx.texture(window_size, components=4)]
        )
        self.channel1 = self.shadertoy.ctx.framebuffer(
            color_attachments=[self.shadertoy.ctx.texture(window_size, components=4)]
        )
        self.shadertoy.channel_0 = self.channel0.color_attachments[0]
        self.shadertoy.channel_1 = self.channel1.color_attachments[0]

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        global worldMouseX, worldMouseY
        worldMouseX, worldMouseY = (
            mouseX + self.sceneCamera.position.x,
            mouseY + self.sceneCamera.position.y,
        )
        self.mc.move(Xinput, Yinput, worldMouseX, worldMouseY)
        camPos = Vec2(
            self.mc.center_x - SCREEN_WIDTH / 2, self.mc.center_y - SCREEN_HEIGHT / 2
        )
        self.sceneCamera.move_to(camPos)
        self.physics_engine.update()
        # Collision is Glitchy

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((50, 50, 50))
        self.channel0.use()
        self.channel0.clear()
        self.sceneCamera.use()
        self.walls.draw()

        self.channel1.use()
        self.channel1.clear()
        # Draw everything that can be hidden in shadows bur does not cast shadow
        # self.walls.draw()

        self.use()
        self.clear()
        self.shadertoy.program['lightPosition'] = Vec2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.shadertoy.program['lightSize'] = 300
        self.shadertoy.program['angle'] = self.mc.angle
        self.shadertoy.render()
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
