import arcade
import arcade.gui
import pyglet.media

import assets
from assets import fonts
from game.config import SCREEN_WIDTH, SCREEN_HEIGHT
from game.entities.player import Player
from game.views import BaseView, return_to_view
from game.views.game_view import GameView
from game.views.gameover import get_gameover_ui
from game.views.menu import get_menu_view_ui
from game.views.pause_menu import get_pause_menu_view_ui
from game.views.settings import get_settings_ui
from game.views.story import get_storybook_ui


class Game(arcade.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.views = None
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        self.bgm: pyglet.media.Player | None = None
        self.change_bgm = False
        self.level: int = 1
        self.music_vol = 1.0
        self.sfx_vol = 1.0
        self.player: Player | None = None

    def setup(self):
        arcade.load_font(fonts.resolve("Melted Monster.ttf"))
        self.bgm = arcade.play_sound(
            assets.sounds.glacier, looping=True, volume=self.music_vol
        )
        self.views = {
            "StartView": {
                # This is the first view, the entrypoint
                "color": arcade.color.BLACK,
                "text": [
                    arcade.Text(
                        "Escape!!",
                        self.width / 2,
                        self.height / 2,
                        font_size=50,
                        anchor_x="center",
                        font_name="Melted Monster",
                    ),
                    arcade.Text(
                        "Click to advance",
                        self.width / 2,
                        self.height / 2 - 75,
                        arcade.color.WHITE,
                        font_size=20,
                        anchor_x="center",
                    ),
                ],
                "next": "MenuView",
            },
            "MenuView": {
                # This shows the menus
                "color": arcade.color.BLACK,
                "bgm": assets.sounds.glacier,
                "text": [
                    arcade.Text(
                        "Escape!!",
                        self.width / 2,
                        self.height - 50,
                        font_size=20,
                        anchor_x="center",
                        font_name="Melted Monster",
                    ),
                ],
                "ui": [
                    get_menu_view_ui(self),
                ],
            },
            "Storybook": {
                # This shows the pre-game storyline
                "color": arcade.color.BLACK,
                "ui": get_storybook_ui(self),
            },
            "GameOver": {
                # This is the GameOver Screen
                "color": (20, 7, 7, 255),
                "ui": get_gameover_ui(self),
            },
            "Settings": {
                # This shows the pre-game storyline
                "keys": return_to_view("MenuView"),
                "color": arcade.color.BLACK,
                "ui": get_settings_ui(self),
            },
            "About": {
                # This shows the about section
                "keys": return_to_view("MenuView"),
                "color": arcade.color.BLACK,
                "text": [
                    arcade.Text(
                        "This is a team submission by BeeTLes for PyWeek35",
                        self.width / 2,
                        self.height / 2,
                        font_size=15,
                        anchor_x="center",
                    ),
                    arcade.Text(
                        "Click to Return",
                        self.width / 2,
                        self.height / 2 - 75,
                        arcade.color.WHITE,
                        font_size=10,
                        anchor_x="center",
                    ),
                ],
                "next": "MenuView",
            },
            "Credits": {
                # This shows the credits section
                "keys": return_to_view("MenuView"),
                "color": arcade.color.BLACK,
                "bgm": assets.sounds.japan,
                "next_bgm_diff": True,
                "text": [
                    arcade.Text(
                        "Here goes credits and contributions, to fill later",
                        self.width / 2,
                        self.height / 2,
                        font_size=15,
                        anchor_x="center",
                    ),
                    arcade.Text(
                        "Click to Return",
                        self.width / 2,
                        self.height / 2 - 75,
                        arcade.color.WHITE,
                        font_size=10,
                        anchor_x="center",
                    ),
                ],
                "next": "MenuView",
            },
            "Levels": {
                # This shows the settings section
                # TODO: implement a proper levels view
                "keys": return_to_view("MenuView"),
                "color": arcade.color.BLACK,
                "text": [
                    arcade.Text(
                        "Level selections here, TODO",
                        self.width / 2,
                        self.height / 2,
                        font_size=15,
                        anchor_x="center",
                    ),
                    arcade.Text(
                        "Click to Return",
                        self.width / 2,
                        self.height / 2 - 75,
                        arcade.color.WHITE,
                        font_size=10,
                        anchor_x="center",
                    ),
                ],
                "next": "MenuView",
            },
            "Pause": {
                # This shows when the game is paused
                "bgm": assets.sounds.tomb,
                "color": arcade.color.BLACK,
                "keys": return_to_view("GameView-same"),
                "text": [
                    arcade.Text(
                        "Escape!!",
                        self.width / 2,
                        self.height - 100,
                        font_size=50,
                        anchor_x="center",
                        font_name="Melted Monster",
                    ),
                ],
                "ui": [
                    get_pause_menu_view_ui(self),
                ],
            },
            # This shows the main game view, starts at level 1
            "GameView": self.get_level_view(1),
            # TODO: Add rest of the Views here
        } | {f"Level-{n}": self.get_level_view(n) for n in range(1, 2)}

        entrypoint = "GameView"  # <- use this for game debug
        view = BaseView(self.views)
        self.show_view(view.configure(entrypoint))
        print("Loading done! Enjoy :) - Team BeaTLes (PyWeek35)")

    @staticmethod
    def get_level_view(level: int) -> GameView:
        return GameView(level)


def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Escape!!")
    game.setup()
    arcade.run()
