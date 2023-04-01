import arcade.gui

import assets
from game.config import LEVEL_COUNT
from game.data import Data
from game.views import change_views


def get_level_menu_view_ui(window: arcade.Window) -> arcade.gui.UIWidget:
    # Create a vertical BoxGroup to align buttons
    levels: list = [None for _ in range(LEVEL_COUNT)]
    # levels_functions: list = [None for i in range(LEVEL_COUNT)]
    jsondata = Data()
    game_data = jsondata.get()
    hp_style = {
        "font_name": "Melted Monster",
        "bg_color": arcade.color.BLACK,
        "font_color": arcade.color.WHITE,
        "border_color_pressed": arcade.color.BLACK,
    }

    def start_level(level: int):
        assets.sounds.click.play()
        print(f"Starting level {level}")
        change_views(window, f"Level{level}")

    layout = arcade.gui.UIBoxLayout(vertical=True)

    # Create 3 rows of buttons with 2 buttons in each row
    for i, _ in enumerate(levels):
        row_layout = arcade.gui.UIBoxLayout(vertical=False)
        if not game_data[f"level_{i + 1}"]["is_locked"]:
            # Create the level buttons
            levels[i] = arcade.gui.UIFlatButton(
                text=f"Level {i + 1}", width=250, style={"font_name": "Melted Monster"}
            )
            # pylint: disable=W0640
            levels[i].on_click = lambda: start_level(i + 1)
            hp_button = arcade.gui.UIFlatButton(
                text=f'HS:{game_data[f"level_{i + 1}"]["high_score"]}',
                width=250,
                style=hp_style,
            )
        else:
            levels[i] = arcade.gui.UIFlatButton(
                text="LOCKED", width=250, style={"font_name": "Melted Monster"}
            )
            hp_button = arcade.gui.UIFlatButton(text="HS: 0", width=250, style=hp_style)
        row_layout.add(levels[i].with_space_around(bottom=20))
        row_layout.add(hp_button.with_space_around(bottom=20))
        layout.add(row_layout)

    # Create the back button
    back_button = arcade.gui.UIFlatButton(
        text="Back",
        width=250,
        style={
            "font_name": "Melted Monster",
            "bg_color": arcade.color.WHITE,
            "font_color": arcade.color.BLACK,
        },
    )

    # noinspection PyUnusedLocal
    @back_button.event("on_click")
    def on_click_back_button(event):
        assets.sounds.click.play(volume=window.sfx_vol)
        change_views(window, "MenuView")

    layout.add(back_button.with_space_around(top=40, bottom=20))

    return arcade.gui.UIAnchorWidget(
        anchor_x="center_x", anchor_y="center_y", child=layout
    )
