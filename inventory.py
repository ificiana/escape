import arcade

from config import SCREEN_HEIGHT, SCREEN_WIDTH, ITEMS, INVENTORY


class InventoryItem(arcade.Sprite):
    def __init__(self, item):
        super().__init__()
        self.texture = arcade.load_texture(f"images/{item}.png")


class InventoryWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Inventory")
        self.inventory_sprites = arcade.SpriteList()

    def setup(self):
        for i, item in enumerate(INVENTORY):
            inventory_item = InventoryItem(item)
            inventory_item.center_x = SCREEN_WIDTH // 2 - 100 + 50 * i
            inventory_item.center_y = SCREEN_HEIGHT // 2
            self.inventory_sprites.append(inventory_item)

    def on_draw(self):
        arcade.start_render()
        self.inventory_sprites.draw()


def main():
    for item in ITEMS:
        INVENTORY.append(item)

    inventory_window = InventoryWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    inventory_window.setup()


if __name__ == "__main__":
    main()
