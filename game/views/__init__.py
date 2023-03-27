from dataclasses import dataclass
from typing import Union, Self

import arcade
from arcade.text_pyglet import FontNameOrNames


@dataclass
class ViewText:
    text: str
    start_x: float
    start_y: float
    color: arcade.Color = arcade.color.WHITE
    font_size: float = 12
    width: int = 0
    align: str = "left"
    font_name: FontNameOrNames = ("calibri", "arial")
    bold: bool = False
    italic: bool = False
    anchor_x: str = "left"
    anchor_y: str = "baseline"
    multiline: bool = False
    rotation: float = 0

    def draw(self):
        arcade.draw_text(
            self.text,
            self.start_x,
            self.start_y,
            self.color,
            self.font_size,
            self.width,
            self.align,
            self.font_name,
            self.bold,
            self.italic,
            self.anchor_x,
            self.anchor_y,
            self.multiline,
            self.rotation,
        )


class BaseView(arcade.View):
    """Customisable View"""

    def __init__(self, views: dict = None):
        super().__init__()
        self.ui_nodes = None
        self.text_nodes: Union[list[ViewText], ViewText, None] = None
        self.bg_color: arcade.csscolor = None
        self.next = None

        # store the views data
        self.views: dict = views or {}

    def configure(self, view: Union[str, arcade.View]) -> "Self":
        """Configure the View"""

        if isinstance(view, arcade.View):
            return view
        self.bg_color = self.views[view].get("color")
        self.text_nodes = self.views[view].get("text")
        self.ui_nodes = self.views[view].get("ui")
        self.next = self.views[view].get("next")
        return self

    def on_show_view(self):
        """This is run once when we switch to this view"""

        arcade.set_background_color(self.bg_color)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

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
            for node in self.ui_nodes:
                self.window.ui_manager.add(node)
            self.window.ui_manager.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """If the user presses the mouse button, navigate to the next View."""

        if self.next:
            self.window.show_view(self.configure(self.next))
