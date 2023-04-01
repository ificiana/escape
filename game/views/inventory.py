from typing import Union

import arcade.gui
from pyglet.math import Vec2

import assets


class Item(arcade.Sprite):
    def __init__(self, sprite_file: str, pos: Vec2, angle: float, name: str = None):
        super().__init__(assets.items.resolve(sprite_file))
        self.name = name or sprite_file.split(".")[0]
        self.center_x, self.center_y = pos
        self.angle = angle

    def get_position(self):
        return Vec2(self.center_x, self.center_y)


class Inventory:
    def __init__(self):
        self.items = {}
        self.quantities = {}

    def add_item(self, item: Item):
        self.items[item.name] = item
        self.quantities[item.name] = self.quantities.get(item.name, 0) + 1
        item.remove_from_sprite_lists()
        print(f"added {item.name} to the inventory")

    def remove_item(self, item_name):
        self.quantities[item_name] = max(self.quantities.get(item_name, 0) - 1, 0)
        if self.quantities[item_name] == 0:
            return self.items.pop(item_name)
        return self.items[item_name]


def get_inventory_ui(
    window: arcade.Window,
) -> Union[arcade.gui.UIWidget, list[arcade.gui.UIWidget]]:
    # Create a horizontal BoxGroup to align buttons
    h_box = arcade.gui.UIBoxLayout(vertical=False)

    text_area0 = arcade.gui.UITextArea(
        x=270,
        y=220,
        width=600,
        height=300,
        text="INVENTORY",
        text_color=arcade.csscolor.WHITE,
        font_size=30,
        font_name="Melted Monster",
    )
    text_area = arcade.gui.UITextArea(
        x=195,
        y=200,
        width=600,
        height=250,
        text="Press ESC to return to Game",
        text_color=arcade.csscolor.WHITE,
        font_size=15,
    )
    text_area1 = arcade.gui.UITextArea(
        x=350,
        y=200,
        width=100,
        height=50,
        text="TODO",
        text_color=arcade.csscolor.WHITE,
        font_size=20,
        font_name="Melted Monster",
    )

    return [
        arcade.gui.UIAnchorWidget(
            anchor_x="center", anchor_y="center", align_y=-50, child=h_box
        ),
        text_area0,
        text_area,
        text_area1,
    ]
