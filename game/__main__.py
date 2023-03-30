import arcade
import arcade.gui

import assets
from game.config import SCREEN_WIDTH, SCREEN_HEIGHT
from game.views import BaseView
from game.views.game_view import GameView
from game.views.inventory import InventoryView
from game.views.menu import get_menu_view_ui
from game.views.pause_menu import get_pause_menu_view_ui
from game.views.story import get_storybook_ui
from game.views.gameover import get_gameover_ui


class Game(arcade.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.views = None
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        self.bgm = None

    def setup(self):
        self.bgm = arcade.play_sound(assets.sounds.whoosh)
        self.bgm.queue(assets.sounds.bg1.source)
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
                "text": [
                    arcade.Text(
                        "Escape!!",
                        self.width / 2,
                        self.height - 50,
                        font_size=20,
                        anchor_x="center",
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
            "About": {
                # This shows the about section
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
                "color": arcade.color.BLACK,
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
            "Settings": {
                # This shows the settings section
                # TODO: implement a proper settings view
                "color": arcade.color.BLACK,
                "text": [
                    arcade.Text(
                        "Here goes settings, TODO",
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
                "bgm": assets.sounds.bg1,
                "color": arcade.color.BLACK,
                "text": [
                    arcade.Text(
                        "Escape!!",
                        self.width / 2,
                        self.height - 100,
                        font_size=50,
                        anchor_x="center",
                    ),
                ],
                "ui": [
                    get_pause_menu_view_ui(self),
                ],
            },
            # This shows the main game view, starts at level 1
            "GameView": self.get_level_view(1),
            # Shows the inventory
            "InventoryView": InventoryView(self),
            # TODO: Add rest of the Views here
        } | {f"Level-{n}": self.get_level_view(n) for n in range(1, 2)}

        entrypoint = "StartView"
        # entrypoint = "GameView"  # <- use this for game debug
        view = BaseView(self.views)
        self.show_view(view.configure(entrypoint))

    @staticmethod
    def get_level_view(level: int) -> GameView:
        return GameView(level)


def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Escape!!")
    game.setup()
    arcade.run()
