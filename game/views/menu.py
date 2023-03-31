import arcade.gui

import assets
from game.views import change_views


def get_menu_view_ui(window: arcade.Window) -> arcade.gui.UIWidget:
    # Create a vertical BoxGroup to align buttons
    v_box = arcade.gui.UIBoxLayout()

    # Create the buttons
    start_button = arcade.gui.UIFlatButton(
        text="New Game", width=250, style={"font_name": "Melted Monster"}
    )
    v_box.add(start_button.with_space_around(bottom=20))

    continue_button = arcade.gui.UIFlatButton(
        text="Continue", width=250, style={"font_name": "Melted Monster"}
    )
    v_box.add(continue_button.with_space_around(bottom=20))

    settings_button = arcade.gui.UIFlatButton(
        text="Settings", width=250, style={"font_name": "Melted Monster"}
    )
    v_box.add(settings_button.with_space_around(bottom=20))

    about_button = arcade.gui.UIFlatButton(
        text="About", width=250, style={"font_name": "Melted Monster"}
    )
    v_box.add(about_button.with_space_around(bottom=20))

    credits_button = arcade.gui.UIFlatButton(
        text="Credits & Contributions", width=250, style={"font_name": "Melted Monster"}
    )
    v_box.add(credits_button.with_space_around(bottom=20))

    quit_button = arcade.gui.UIFlatButton(
        text="Quit", width=250, style={"font_name": "Melted Monster"}
    )
    v_box.add(quit_button)

    # noinspection PyUnusedLocal
    @start_button.event("on_click")
    def on_click_start(event):
        assets.sounds.click.play()
        change_views(window, "Storybook")

    # noinspection PyUnusedLocal
    @about_button.event("on_click")
    def on_click_about(event):
        assets.sounds.click.play()
        change_views(window, "About")

    # noinspection PyUnusedLocal
    @quit_button.event("on_click")
    def on_click_quit(event):
        arcade.exit()

    # noinspection PyUnusedLocal
    @settings_button.event("on_click")
    def on_click_settings(event):
        assets.sounds.click.play()
        change_views(window, "Settings")

    # noinspection PyUnusedLocal
    @credits_button.event("on_click")
    def on_click_credits(event):
        assets.sounds.click.play()
        window.change_bgm = True
        change_views(window, "Credits")

    # noinspection PyUnusedLocal
    @continue_button.event("on_click")
    def on_click_continue(event):
        assets.sounds.click.play()
        change_views(window, "Levels")

    return arcade.gui.UIAnchorWidget(
        anchor_x="center_x", anchor_y="center_y", child=v_box
    )


def return_to_menu_binding(window: arcade.Window, key):
    match key:
        case arcade.key.ESCAPE:
            assets.sounds.click.play()
            change_views(window, "MenuView")
