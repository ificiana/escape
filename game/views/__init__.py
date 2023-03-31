from typing import Union, Self

import arcade

import assets
from game.sounds import change_music


class BaseView(arcade.View):
    """Customisable View"""

    def __init__(self, views: dict = None):
        super().__init__()
        self.ui_nodes = None
        self.text_nodes: Union[list[arcade.Text], arcade.Text, None] = None
        self.bg_color: arcade.csscolor = None
        self.next = None
        self.bgm = None

        # store the views data
        self.views: dict = views or {}

    def configure(self, view: str) -> "Self":
        """Configure the View"""
        if isinstance(self.views[view], arcade.View):
            return self.views[view]
        self.bg_color = self.views[view].get("color")
        self.text_nodes = self.views[view].get("text")
        self.ui_nodes = self.views[view].get("ui")
        self.next = self.views[view].get("next")
        self.bgm = self.views[view].get("bgm")
        return self

    def on_show_view(self):
        """This is run once when we switch to this view"""

        arcade.set_background_color(self.bg_color)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        if self.bgm:
            self.window.bgm = change_music(self.window.bgm, self.bgm)

    def on_hide_view(self):
        pass

    def on_draw(self):
        """Draw this view"""

        self.clear()

        # loop through the nodes and draw them
        if self.text_nodes:
            for node in self.text_nodes:
                node.draw()

        if self.ui_nodes:
            self.window.ui_manager.clear()
            for node in self.ui_nodes:
                self.window.ui_manager.add(node)
            self.window.ui_manager.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """If the user presses the mouse button, navigate to the next View."""

        if self.next:
            self.window.bgm = change_music(self.window.bgm, assets.sounds.bg1)
            self.window.ui_manager.clear()
            self.window.show_view(self.configure(self.next))


def change_views(window: arcade.Window, dest_view: str):
    window.ui_manager.clear()
    window.show_view(BaseView(window.views).configure(dest_view))
