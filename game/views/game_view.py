import time

import arcade
from pyglet.math import Vec2

import assets
from game.entities.player import Player
from game.sounds import change_music
from game.views import change_views

arcade.enable_timings()


class GameView(arcade.View):
    """The game window"""

    def __init__(self, level):
        super().__init__()

        # declare objects and entities
        self.walls = None
        self.player = None
        self.physics_engine = None
        self.start_time = None

        # movement states
        self.movement = Vec2(0, 0)
        self.mouse_pos = Vec2(0, 0)

        # sprite lists
        self.entities_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Setup camera
        self.scene_camera = arcade.Camera(*self.window.size)
        self.gui_camera = arcade.Camera(*self.window.size)

        # select the level
        self.select_level(level)

    def select_level(self, level: int = 1):
        """Select the level and set up the game view"""
        level_map = arcade.TileMap(
            assets.tilemaps.resolve(f"level{level}.tmx"), use_spatial_hash=True
        )

        # place objects
        self.walls = level_map.sprite_lists["walls"]

        # Set up the player
        self.player = Player()
        self.player.center_x = self.window.width / 2
        self.player.center_y = self.window.height / 2
        self.entities_list.append(self.player)

        # Create physics engine for collision
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.walls)

        # Start time
        self.start_time = time.time()

    def on_show_view(self):
        """This is run once when we switch to this view"""

        # set game background
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.window.bgm = change_music(self.window.bgm, assets.sounds.bg2, looping=True)

    def screen_to_world_point(self, screen_point: Vec2):
        return screen_point + self.scene_camera.position

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # Use the mouse to look around
        self.mouse_pos.x, self.mouse_pos.y = x, y

    def on_update(self, delta_time: float):
        self.player.move(*self.movement, *self.screen_to_world_point(self.mouse_pos))
        cam_pos = Vec2(
            self.player.center_x - self.window.width / 2,
            self.player.center_y - self.window.height / 2,
        )
        self.scene_camera.move_to(cam_pos)
        self.physics_engine.update()

    def on_key_press(self, symbol: int, modifiers: int):
        """Handle Keyboard Input."""
        # Navigate with WASD or Arrow keys"""
        match symbol:
            case arcade.key.DOWN | arcade.key.S:
                self.movement.y = -1
            case arcade.key.UP | arcade.key.W:
                self.movement.y = 1
            case arcade.key.LEFT | arcade.key.A:
                self.movement.x = -1
            case arcade.key.RIGHT | arcade.key.D:
                self.movement.x = 1
            case arcade.key.Q:
                self.player.attack(self.entities_list)
            case arcade.key.I:
                print("Open Inventory: ")
                assets.sounds.click.play()
                change_views(self.window, "InventoryView")
            case arcade.key.ESCAPE:
                print("Pause Game: ")
                assets.sounds.click.play()
                change_views(self.window, "Pause")

        # add fail-check
        self.movement.clamp(-1, 1)

    def on_key_release(self, symbol: int, modifiers: int):
        match symbol:
            case arcade.key.DOWN | arcade.key.S:
                self.movement.y = 0
            case arcade.key.UP | arcade.key.W:
                self.movement.y = 0
            case arcade.key.LEFT | arcade.key.A:
                self.movement.x = 0
            case arcade.key.RIGHT | arcade.key.D:
                self.movement.x = 0

            # add fail-check
        self.movement.clamp(-1, 1)

    def on_draw(self):
        """Draw this view"""

        # clean view
        self.clear()

        self.scene_camera.use()
        self.entities_list.draw()
        self.walls.draw()

        # Add GUI
        self.gui_camera.use()
        arcade.Text(
            f"Health: 100, Time: "
            f"{':'.join(map(lambda x: f'{int(x):02d}',divmod(time.time()-self.start_time, 60)))}",
            self.window.width - 200,
            self.window.height - 25,
        ).draw()
        arcade.Text(
            f"FPS: {int(arcade.get_fps())}",
            20,
            self.window.height - 25,
        ).draw()
        arcade.Text("Press ESC to pause; press I to enter the inventory", 10, 10).draw()
