from typing import Union

import arcade.gui

import assets


def get_settings_ui() -> Union[arcade.gui.UIWidget, list[arcade.gui.UIWidget]]:
    # Create a vertical BoxGroup to align buttons
    h_box = arcade.gui.UIBoxLayout(vertical=False)

    text_area0 = arcade.gui.UITextArea(
        x=270,
        y=220,
        width=600,
        height=300,
        text="SETTINGS",
        text_color=arcade.csscolor.WHITE,
        font_size=30,
        font_name="Melted Monster",
    )
    text_area = arcade.gui.UITextArea(
        x=180,
        y=180,
        width=600,
        height=250,
        text="Press ESC to return to main menu.",
        text_color=arcade.csscolor.WHITE,
        font_size=15,
    )
    text_area1 = arcade.gui.UITextArea(
        x=180,
        y=200,
        width=50,
        height=50,
        text="SFX",
        text_color=arcade.csscolor.WHITE,
        font_size=20,
        font_name="Melted Monster",
    )
    text_area2 = arcade.gui.UITextArea(
        x=480,
        y=200,
        width=80,
        height=50,
        text="MUSIC",
        text_color=arcade.csscolor.WHITE,
        font_size=20,
        font_name="Melted Monster",
    )

    # Create the buttons
    reduce_sfx_button = arcade.gui.UIFlatButton(text="-", width=50)
    h_box.add(reduce_sfx_button.with_space_around(right=70))

    inc_sfx_button = arcade.gui.UIFlatButton(text="+", width=50)
    h_box.add(inc_sfx_button.with_space_around(right=50))

    reduce_music_button = arcade.gui.UIFlatButton(text="-", width=50)
    h_box.add(reduce_music_button.with_space_around(left=80))

    inc_music_button = arcade.gui.UIFlatButton(text="+", width=50)
    h_box.add(inc_music_button.with_space_around(left=80))

    @reduce_sfx_button.event("on_click")
    def on_click_reduce_sfx(event):
        print("Prev:", event)
        # TODO: Greyout if cur_page = 1
        assets.sounds.click.play()

    @inc_sfx_button.event("on_click")
    def on_click_inc_sfx(event):
        print("Next:", event)
        assets.sounds.click.play()

    @reduce_music_button.event("on_click")
    def on_click_reduce_music(event):
        print("Prev:", event)
        # TODO: Greyout if cur_page = 1
        assets.sounds.click.play()

    @inc_music_button.event("on_click")
    def on_click_inc_music(event):
        print("Next:", event)
        assets.sounds.click.play()

    return [
        arcade.gui.UIAnchorWidget(
            anchor_x="center", anchor_y="center", align_y=-50, child=h_box
        ),
        text_area0,
        text_area,
        text_area1,
        text_area2,
    ]
