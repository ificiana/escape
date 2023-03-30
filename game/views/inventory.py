import arcade

import assets
from game.views import change_views


class InventoryView(arcade.View):
    def __init__(self, game, items=None):
        super().__init__()
        self.game = game
        self.items = items or []
        self.selected_item = None
        self.show_menu = False
        self.background_sprite = None
        self.close_button_sprite = None

        self.setup()

    def setup(self):
        # Create a background sprite
        if self.background_sprite is None:
            self.background_sprite = arcade.SpriteSolidColor(
                *self.game.size, arcade.color.GRAY
            )

        # Create a close button sprite
        if self.close_button_sprite is None:
            self.close_button_sprite = arcade.Sprite(
                ":resources:onscreen_controls/shaded_light/close.png"
            )
            self.close_button_sprite.center_x = self.game.width - 50
            self.close_button_sprite.center_y = 50

    def on_draw(self):
        arcade.start_render()
        self.background_sprite.draw()
        arcade.draw_text(
            "Inventory",
            self.game.width / 2,
            self.game.height - 40,
            arcade.color.BLACK,
            28,
            anchor_x="center",
        )

        # Draw items
        for i, item in enumerate(self.items):
            item_sprite = arcade.Sprite(assets.items.resolve(f"{item}.png"))
            # item_sprite = arcade.Sprite(f"assets/items/{item}.png")
            item_sprite.name = item
            item_sprite.center_x = 80
            item_sprite.center_y = 510 - i * 100
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

    def on_mouse_press(self, x, y, button, modifiers):
        if (
            button == arcade.MOUSE_BUTTON_LEFT
            and self.close_button_sprite.collides_with_point((x, y))
            and isinstance(self.game.current_view, InventoryView)
        ):
            change_views(self.game, "GameView")

    def on_key_press(self, symbol, modifiers):
        match symbol:
            case arcade.key.ESCAPE:
                change_views(self.game, "GameView")
