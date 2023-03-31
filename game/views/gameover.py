from typing import Union

import arcade.gui

import assets
from game.views import change_views


# pylint: disable=R0801


def get_gameover_ui(
    window: arcade.Window,
) -> Union[arcade.gui.UIWidget, list[arcade.gui.UIWidget]]:
    # Create a vertical BoxGroup to align buttons
    h_box = arcade.gui.UIBoxLayout(vertical=True)

    text_area = arcade.gui.UITextArea(
        x=100,
        y=200,
        width=window.width,
        height=300,
        text="GAME OVER",
        text_color=(255, 160, 160, 255),
        font_size=76,
        font_name="Melted Monster",
    )

    # Create the buttons
    restart_button = arcade.gui.UIFlatButton(text="Restart", width=200)
    h_box.add(restart_button.with_space_around(bottom=20))

    menu_button = arcade.gui.UIFlatButton(text="Main Menu", width=200)
    h_box.add(menu_button.with_space_around(bottom=40))

    # noinspection PyUnusedLocal
    @menu_button.event("on_click")
    def on_click_menu(event):
        assets.sounds.click.play()
        window.change_bgm = True
        change_views(window, "MenuView")

    # noinspection PyUnusedLocal
    @restart_button.event("on_click")
    def on_click_restart(event):
        assets.sounds.click.play()
        change_views(window, "GameView")

    return [
        arcade.gui.UIAnchorWidget(anchor_x="center", anchor_y="bottom", child=h_box),
        text_area,
    ]
