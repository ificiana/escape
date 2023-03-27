import arcade


class Inventory:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items
        self.selected_item = None
        self.show_menu = False

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
        if show:
            self.show_menu = True
            menu_text = "Inventory\n\n"
            for item in self.items:
                if item == self.selected_item:
                    menu_text += f"> {item}\n"
                else:
                    menu_text += f"  {item}\n"

            arcade.start_render()
            arcade.draw_text(menu_text, 100, 400, arcade.color.WHITE, 20)
            arcade.finish_render()
        else:
            self.show_menu = False

    def handle_key_press(self, key):
        if key == arcade.key.I:
            self.display_menu(not self.show_menu)
