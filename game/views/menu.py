import arcade.gui

from game.views import change_views


def get_menu_view_ui(window: arcade.Window) -> arcade.gui.UIWidget:
    # Create a vertical BoxGroup to align buttons
    v_box = arcade.gui.UIBoxLayout()

    # Create the buttons
    start_button = arcade.gui.UIFlatButton(text="New Game", width=250)
    v_box.add(start_button.with_space_around(bottom=20))

    continue_button = arcade.gui.UIFlatButton(text="Continue", width=250)
    v_box.add(continue_button.with_space_around(bottom=20))

    settings_button = arcade.gui.UIFlatButton(text="Settings", width=250)
    v_box.add(settings_button.with_space_around(bottom=20))

    about_button = arcade.gui.UIFlatButton(text="About", width=250)
    v_box.add(about_button.with_space_around(bottom=20))

    credits_button = arcade.gui.UIFlatButton(text="Credits & Contributions", width=250)
    v_box.add(credits_button.with_space_around(bottom=20))

    quit_button = arcade.gui.UIFlatButton(text="Quit", width=250)
    v_box.add(quit_button)

    @start_button.event("on_click")
    def on_click_start(event):
        print("Start:", event)
        change_views(window, "Storybook")

    @about_button.event("on_click")
    def on_click_about(event):
        print("About:", event)
        change_views(window, "About")

    @quit_button.event("on_click")
    def on_click_quit(event):
        print("Quit:", event)
        arcade.exit()

    @settings_button.event("on_click")
    def on_click_settings(event):
        print("Settings:", event)
        change_views(window, "Settings")

    @credits_button.event("on_click")
    def on_click_credits(event):
        print("Credits:", event)
        change_views(window, "Credits")

    @continue_button.event("on_click")
    def on_click_continue(event):
        print("Continue:", event)
        change_views(window, "Levels")

    return arcade.gui.UIAnchorWidget(
        anchor_x="center_x", anchor_y="center_y", child=v_box
    )
