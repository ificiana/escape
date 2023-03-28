import arcade
import arcade.gui

from game.config import *
from game.views import ViewText, BaseView
from game.views.game_view import GameView
from game.views.menu import get_menu_view_ui
from game.views.story import get_storybook_ui


class Game(arcade.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.views = None
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        self.game_view = GameView()

    def setup(self):
        self.views = {
            "StartView": {
                # This is the first view, the entrypoint
                "color": arcade.color.BLACK,
                "text": [
                    ViewText(
                        "Escape!!",
                        self.width / 2,
                        self.height / 2,
                        font_size=50,
                        anchor_x="center",
                    ),
                    ViewText(
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
                    ViewText(
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
                    ViewText(
                        "This is a team submission by BeeTLes for PyWeek35",
                        self.width / 2,
                        self.height / 2,
                        font_size=15,
                        anchor_x="center",
                    ),
                    ViewText(
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
            # This shows the main game view
            "GameView": self.game_view,
            # TODO: Add rest of the Views here
        }

        entrypoint = "StartView"
        view = BaseView(self.views)
        self.show_view(view.configure(entrypoint))


def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Escape!!")
    game.setup()
    arcade.run()
