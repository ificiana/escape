from time import time

import arcade
from pyglet.math import Vec2

import assets
from game.entities.player import Player
from game.entities.enemy import Enemy
from game.sounds import change_music
from game.views import change_views
from game.views.inventory import Item

arcade.enable_timings()


class GameView(arcade.View):
    """The game window"""

    def __init__(self, level):
        super().__init__()

        # declare objects and entities
        self.cur_item = None
        self.walls = None
        self.floor = None
        self.objects = None
        self.pickables = None
        self.player = None
        self.physics_engine = None
        self.start_time = None
        self.bgm = None

        # special purpose bgm
        self.bgm2 = None

        # in game text popup
        self.display_text = ""

        # movement states
        self.movement = Vec2(0, 0)
        self.mouse_pos = Vec2(0, 0)

        # sprite lists
        self.enemies = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Setup camera
        self.scene_camera = arcade.Camera(*self.window.size)
        self.gui_camera = arcade.Camera(*self.window.size)

        # select the level
        self.select_level(level)

    def select_level(self, level: int = 1):
        """Select the level and set up the game view"""

        use_guided_path = True

        # if guided path is used, enemies get stuck to the wall...
        # if not used, the enemies just fly past like jets!!? huh? fixme

        #### Fixed you. enemies never get stuck to wall.
        # No need of physics engine for enemies. Game runs faster

        # I'll let you choose what to keep

        level_map = arcade.TileMap(
            # assets.tilemaps.resolve(f"level{level}.tmx"), use_spatial_hash=True,  # <- real one
            assets.tilemaps.resolve(
                "level1.tmx" if use_guided_path else "level1.tmx"
            ),  # <- test
            use_spatial_hash=True,
        )
        self.window.level = level

        # place objects
        self.floor = level_map.sprite_lists["floor"]
        self.walls = level_map.sprite_lists["walls"]
        self.objects = level_map.sprite_lists["objects"]
        self.pickables = arcade.SpriteList(use_spatial_hash=True)

        if level_map.sprite_lists.get("pickables") is not None:
            for item in level_map.sprite_lists["pickables"]:
                self.pickables.append(
                    Item(item.properties["file"], Vec2(*item.position), item.angle)
                )

        # Set up the player
        self.player = Player(self)
        self.player.position = level_map.sprite_lists["player"][0].position

        # Set up the enemies
        if use_guided_path:
            arrows = [
                level_map.sprite_lists["arrow_left"],
                level_map.sprite_lists["arrow_right"],
                level_map.sprite_lists["arrow_up"],
                level_map.sprite_lists["arrow_down"],
            ]
        else:
            arrows = None

        barriers = [self.walls, self.objects]

        for enemy in level_map.sprite_lists["enemies"]:
            if use_guided_path:
                e = Enemy(
                    initial_pos=enemy.position,
                    arrows=arrows,
                    barriers=barriers,
                    game_view=self,
                )
            else:
                e = Enemy(initial_pos=enemy.position, barriers=barriers, game_view=self)
            self.enemies.append(e)

        # Create physics engine for collision
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, barriers)

        # Start time
        self.start_time = time()

    def remove_enemy_from_world(self, enemy: Enemy):
        self.enemies.remove(enemy)

    def set_display_text(self, text: str):
        self.display_text = text

    def on_show_view(self):
        """This is run once when we switch to this view"""

        # set game background
        arcade.set_background_color(arcade.csscolor.BLACK)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.window.bgm = change_music(
            self.window,
            self.window.bgm,
            assets.sounds.horror,
            looping=True,
            volume=0.2,
            speed=0.5,
        )
        if self.bgm is None:
            self.bgm = change_music(
                self.window, self.bgm, assets.sounds.heart, volume=0.6, looping=True
            )
            # self.bgm2 = change_music(self.window, self.bgm2,
            # assets.sounds.insomnia, volume=0.2, looping=True)
        else:
            self.bgm.play()
            # self.bgm2.play()

    def on_hide_view(self):
        self.bgm.pause()
        # self.bgm2.pause()

    def screen_to_world_point(self, screen_point: Vec2):
        return screen_point + self.scene_camera.position

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # Use the mouse to look around
        self.mouse_pos.x, self.mouse_pos.y = x, y

    def on_update(self, delta_time: float):
        self.player.move(self.movement, self.screen_to_world_point(self.mouse_pos))
        self.player.update_player()
        cam_pos = Vec2(
            self.player.center_x - self.window.width / 2,
            self.player.center_y - self.window.height / 2,
        )
        self.scene_camera.move_to(cam_pos)
        self.physics_engine.update()

        self.enemies.update()

    def gameover(self):
        change_views(self.window, "GameOver")

    def on_key_press(self, symbol: int, modifiers: int):
        """Handle Keyboard Input."""

        # Navigate with WASD or Arrow keys

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
                self.player.attack()
            case arcade.key.G:
                self.gameover()
            case arcade.key.I:
                assets.sounds.click.play(volume=self.window.sfx_vol)
                change_views(self.window, "InventoryView")
            case arcade.key.F:
                if self.cur_item:
                    assets.sounds.click.play(volume=self.window.sfx_vol)
                    self.display_text = ""
                    self.player.inventory.add_item(self.cur_item)
                    self.cur_item = None
            case arcade.key.ESCAPE:
                assets.sounds.click.play(volume=self.window.sfx_vol)
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
        if self.floor is not None:
            self.floor.draw()
        self.walls.draw()
        if self.objects is not None:
            self.objects.draw()
        if self.pickables is not None:
            self.pickables.draw()
        self.enemies.draw()

        # TODO: remove this after debug
        for i in self.walls:
            i.draw_hit_box()
        if self.enemies[0].arrows:
            for i in self.enemies[0].arrows:
                for j in i:
                    j.draw_hit_box()

        self.player.draw()

        # Add GUI
        self.gui_camera.use()
        arcade.Text(
            f"Health: 100, Time: "
            f"{':'.join(map(lambda x: f'{int(x):02d}', divmod(time() - self.start_time, 60)))}",
            self.window.width - 200,
            self.window.height - 25,
        ).draw()
        arcade.Text(
            f"FPS: {int(arcade.get_fps())}",
            20,
            self.window.height - 25,
        ).draw()
        arcade.Text("Press ESC to pause; press I to enter the inventory", 10, 10).draw()
        arcade.Text(
            self.display_text,
            0,
            self.window.height / 2 + 100,
            width=self.window.width,
            align="center",
            font_size=24,
            bold=True,
            color=arcade.color.WHITE,
        ).draw()
