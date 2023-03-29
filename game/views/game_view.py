import arcade
from pyglet.math import clamp, Vec2

# from arcade.experimental.shadertoy import Shadertoy
import assets

from game.inventory import Inventory
from game.config import *
from game.entities import Player

# pylint: disable=global-statement
# TODO: fix this

x_input, y_input = 0, 0
mouseX, mouseY = 0, 0
worldMouseX, worldMouseY = mouseX, mouseY


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = Player()
        tile_map = arcade.TileMap(
            assets.tilemaps.resolve("level1.tmx"), use_spatial_hash=True
        )
        self.walls = tile_map.sprite_lists["walls"]

        # Setup camera
        self.sceneCamera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Create physics engine for collision
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.walls)

        # Setup inventory
        self.inventory = Inventory()

        # Shader related work
        # self.shadertoy = None
        # self.channel0 = None
        # self.channel1 = None
        # self.load_shader()

    def setup(self):
        # Initial items the player has
        self.inventory.add_item("Knife")

    # def load_shader(self):
    #     shader_file_path = assets.sprites.resolve("shadow.glsl")
    #     window_size = self.get_size()
    #     self.shadertoy = Shadertoy.create_from_file(window_size, shader_file_path)
    #     self.channel0 = self.shadertoy.ctx.framebuffer(
    #         color_attachments=[self.shadertoy.ctx.texture(window_size, components=4)]
    #     )
    #     self.channel1 = self.shadertoy.ctx.framebuffer(
    #         color_attachments=[self.shadertoy.ctx.texture(window_size, components=4)]
    #     )
    #     self.shadertoy.channel_0 = self.channel0.color_attachments[0]
    #     self.shadertoy.channel_1 = self.channel1.color_attachments[0]

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        global worldMouseX, worldMouseY
        worldMouseX, worldMouseY = (
            mouseX + self.sceneCamera.position.x,
            mouseY + self.sceneCamera.position.y,
        )
        self.player.move(x_input, y_input, worldMouseX, worldMouseY)
        cam_pos = Vec2(
            self.player.center_x - SCREEN_WIDTH / 2,
            self.player.center_y - SCREEN_HEIGHT / 2,
        )
        self.sceneCamera.move_to(cam_pos)
        self.physics_engine.update()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        # self.channel0.use()
        # self.channel0.clear()
        self.sceneCamera.use()
        self.walls.draw()

        # self.channel1.use()
        # self.channel1.clear()
        # Draw everything that can be hidden in shadows bur does not cast shadow
        # self.walls.draw()

        # self.use()
        self.clear()
        # self.shadertoy.program["lightPosition"] = Vec2(
        #     SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        # )
        # self.shadertoy.program["lightSize"] = 300
        # self.shadertoy.program["angle"] = self.player.angle
        # self.shadertoy.render()
        self.player.draw()
        self.walls.draw()
        self.inventory.display_menu(self.inventory.show_menu)

    # Handle Keyboard Input
    # Navigate with WASD or Arrow keys and use Mouse for direction
    def on_key_press(self, symbol: int, modifiers: int):
        global x_input, y_input
        if symbol in [arcade.key.DOWN, arcade.key.S]:
            y_input = -1
        if symbol in [arcade.key.UP, arcade.key.W]:
            y_input = 1
        if symbol in [arcade.key.LEFT, arcade.key.A]:
            x_input = -1
        if symbol in [arcade.key.RIGHT, arcade.key.D]:
            x_input = 1
        x_input = clamp(x_input, -1, 1)
        self.inventory.handle_key_press(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        global x_input, y_input
        if symbol in [arcade.key.DOWN, arcade.key.S]:
            y_input = 0
        if symbol in [arcade.key.UP, arcade.key.W]:
            y_input = 0
        if symbol in [arcade.key.LEFT, arcade.key.A]:
            x_input = 0
        if symbol in [arcade.key.RIGHT, arcade.key.D]:
            x_input = 0
        x_input = clamp(x_input, -1, 1)

    # Handle Mouse Events
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        global mouseX, mouseY, worldMouseX, worldMouseY
        mouseX, mouseY = x, y
        worldMouseX, worldMouseY = (
            mouseX + self.sceneCamera.position.x,
            mouseY + self.sceneCamera.position.y,
        )
