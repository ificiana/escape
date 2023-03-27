import arcade

from .config import SCREEN_HEIGHT, SCREEN_WIDTH


class Inventory:
    def __init__(self):
        self.is_open = False
        self.inventory_sprites = arcade.SpriteList()

    def add_item(self, item):
        inventory_item = arcade.Sprite(f"assets/items/{item}.png")
        inventory_item.center_x = SCREEN_WIDTH // 2
        inventory_item.center_y = SCREEN_HEIGHT // 2
        self.inventory_sprites.append(inventory_item)

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def on_key_press(self, key, modifiers):
        if key == arcade.key.I:
            self.open()
        elif key == arcade.key.ESCAPE:
            self.close()

    def draw(self):
        if self.is_open:
            self.inventory_sprites.draw()
