import arcade
import arcade.gui

from game.config import *
from game.views import BaseView
from game.views.game_view import GameView
from game.views.inventory import InventoryView
from game.views.menu import get_menu_view_ui
from game.views.story import get_storybook_ui


class Game(arcade.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.views = None
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        self.inventory_view = InventoryView(self)

    def setup(self):
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
            # This shows the main game view, starts at level 1
            "GameView": self.get_level_view(1),
            # Shows the inventory
            "InventoryView": self.inventory_view,
            # TODO: Add rest of the Views here
        } | {f"Level-{n}": self.get_level_view(n) for n in range(1, 2)}

        entrypoint = "StartView"
        # entrypoint = "GameView"  # <- use this for game debug
        view = BaseView(self.views)
        self.show_view(view.configure(entrypoint))

    @staticmethod
    def get_level_view(level: int) -> GameView:
        return GameView(level)

    def show_game_view(self):
        self.show_view(self.game_view)

    def show_inventory_view(self):
        self.show_view(self.inventory_view)

    def hide_inventory_view(self):
        self.show_game_view()


def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Escape!!")
    game.setup()
    arcade.run()
