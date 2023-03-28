import arcade

from .config import SCREEN_WIDTH, SCREEN_HEIGHT


class Inventory:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items
        self.selected_item = None
        self.show_menu = False
        self.background_sprite = None
        self.close_button_sprite = None

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
        else:
            print(f"{item} is already in the inventory.")

    def select_item(self, item):
        if item in self.items:
            self.selected_item = item
        else:
            print(f"{item} is not in the inventory.")

    def display_menu(self, show=True):
        self.show_menu = show
        if show:
            # Create a background sprite
            if self.background_sprite is None:
                self.background_sprite = arcade.SpriteSolidColor(
                    SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.GRAY
                )

            # Create a close button sprite
            if self.close_button_sprite is None:
                self.close_button_sprite = arcade.Sprite(
                    ":resources:onscreen_controls/shaded_light/close.png"
                )
                self.close_button_sprite.center_x = SCREEN_WIDTH - 50
                self.close_button_sprite.center_y = 50

            # Create a sprite for each item
            item_sprites = []
            for item in self.items:
                item_sprite = arcade.Sprite(f"assets/items/{item}.png")
                item_sprite.name = item
                item_sprite.center_x = 80
                item_sprite.center_y = 510 - len(item_sprites) * 100
                item_sprites.append(item_sprite)

            # Render the menu
            arcade.set_background_color(arcade.color.WHITE)
            arcade.start_render()
            self.background_sprite.draw()
            arcade.draw_text(
                "Inventory",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT - 40,
                arcade.color.BLACK,
                28,
                anchor_x="center",
            )
            for item_sprite in item_sprites:
                item_sprite.draw()
                arcade.draw_text(
                    item_sprite.name,
                    item_sprite.center_x,
                    item_sprite.center_y - 50,
                    arcade.color.BLACK,
                    14,
                    anchor_x="center",
                )
            self.close_button_sprite.draw()
            arcade.finish_render()

    def handle_mouse_press(self, x, y, button):
        if self.show_menu and button == arcade.MOUSE_BUTTON_LEFT:
            if self.close_button_sprite.collides_with_point((x, y)):
                self.display_menu(False)

    def handle_key_press(self, key):
        if key == arcade.key.I:
            self.display_menu(not self.show_menu)
        elif key == arcade.key.ESCAPE:
            self.display_menu(False)
