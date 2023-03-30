import arcade.gui

import assets
from game.sounds import change_music
from game.views import change_views


def get_pause_menu_view_ui(window: arcade.Window) -> arcade.gui.UIWidget:
    # Create a vertical BoxGroup to align buttons
    v_box = arcade.gui.UIBoxLayout()

    # Create the buttons
    resume_button = arcade.gui.UIFlatButton(text="Resume", width=250)
    v_box.add(resume_button.with_space_around(bottom=20))

    inventory_button = arcade.gui.UIFlatButton(text="Inventory", width=250)
    v_box.add(inventory_button.with_space_around(bottom=20))

    quit_button = arcade.gui.UIFlatButton(text="Quit to main menu", width=250)
    v_box.add(quit_button)

    @resume_button.event("on_click")
    def on_click_start(event):
        assets.sounds.click.play()
        change_views(window, "GameView")

    @quit_button.event("on_click")
    def on_click_quit(event):
        assets.sounds.click.play()
        window.bgm = change_music(window.bgm, assets.sounds.bg1, looping=True)
        change_views(window, "MenuView")

    @inventory_button.event("on_click")
    def on_click_settings(event):
        assets.sounds.click.play()
        change_views(window, "InventoryView")

    return arcade.gui.UIAnchorWidget(
        anchor_x="center_x", anchor_y="center_y", child=v_box
    )
