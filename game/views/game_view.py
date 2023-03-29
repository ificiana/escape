import arcade
from pyglet.math import clamp, Vec2

import assets
from game.torch import TorchShaderToy  # Import the TorchShaderToy class from torch.py
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

        # Create an instance of TorchShaderToy and set its position and radius
        self.torch = TorchShaderToy()
        self.torch.set_torch_pos(0.5, 0.5)
        self.torch.set_torch_radius(0.2)

    def setup(self):
        # Initial items the player has
        self.inventory.add_item("Knife")

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

        # Set the position of the torch to the player's position
        self.torch.set_torch_pos(
            self.player.center_x / SCREEN_WIDTH, self.player.center_y / SCREEN_HEIGHT
        )

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        self.sceneCamera.use()
        self.walls.draw()

        self.clear()

        # Draw the player sprite
        self.player.draw()

        # Render the torch shader program on the player sprite
        with self.torch:
            self.torch.set_resolution(self.player.width, self.player.height)
            self.torch.set_light_intensity(1.0)
            self.torch.render(self.player.center_x, self.player.center_y)

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
