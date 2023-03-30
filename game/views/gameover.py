from typing import Union

import arcade.gui

import assets
from assets import fonts
from game.views import change_views
from game.sounds import change_music


def get_gameover_ui(
    window: arcade.Window,
) -> Union[arcade.gui.UIWidget, list[arcade.gui.UIWidget]]:
    # Create a vertical BoxGroup to align buttons
    h_box = arcade.gui.UIBoxLayout(vertical=True)

    arcade.load_font(fonts.resolve("Melted Monster.ttf"))
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

    @menu_button.event("on_click")
    def on_click_menu(event):
        assets.sounds.click.play()
        window.bgm = change_music(window.bgm, assets.sounds.bg1, looping=True)
        change_views(window, "MenuView")
        

    @restart_button.event("on_click")
    def on_click_restart(event):
        print("Restart:", event)
        assets.sounds.click.play()
        # TODO: Reset the level and all entities
        change_views(window, "GameView")

    return [
        arcade.gui.UIAnchorWidget(anchor_x="center", anchor_y="bottom", child=h_box),
        text_area,
    ]
