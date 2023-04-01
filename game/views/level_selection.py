import arcade.gui
import assets
from game.views import change_views
from game.config import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_COUNT
from game.data import data


def get_level_menu_view_ui(window: arcade.Window) -> arcade.gui.UIWidget:
    # Create a vertical BoxGroup to align buttons
    levels:list =[ None for i in range(LEVEL_COUNT)]
    levels_functions:list =[ None for i in range(LEVEL_COUNT)]
    jsondata=data()
    game_data=jsondata.get()
    hp_style={
        "font_name": "Melted Monster",
        "bg_color": arcade.color.BLACK,
        "font_color": arcade.color.WHITE,
        "border_color_pressed":arcade.color.BLACK
    }
    def start_level(level:int):
        assets.sounds.click.play()
        print(f"Starting level {level}")
        change_views(window, f"Level{level}")


    start_level_1=lambda a: start_level(1)
    start_level_2=lambda a: start_level(2)
    start_level_3=lambda a: start_level(3)
    start_level_4=lambda a: start_level(4)

    layout = arcade.gui.UIBoxLayout(vertical=True)


    # Create 3 rows of buttons with 2 buttons in each row
    for i in range(len(levels)):
        row_layout = arcade.gui.UIBoxLayout(vertical=False)
        if(game_data[f"level_{i+1}"]["is_locked"]==False):
        # Create the level buttons
            levels[i] = arcade.gui.UIFlatButton(
                text=f"Level {i+1}", width=250, style={"font_name": "Melted Monster"}
            )
            levels[i].on_click = eval(f"start_level_{i+1}")
            hp_button = arcade.gui.UIFlatButton(
                text=f'HS:{game_data[f"level_{i+1}"]["high_score"]}', width=250, style=hp_style
            )
        else:
            levels[i] = arcade.gui.UIFlatButton(
                text=f"LOCKED", width=250, style={"font_name": "Melted Monster"}
            )
            hp_button = arcade.gui.UIFlatButton(
                text=f"HS: 0", width=250, style=hp_style
            )
        row_layout.add(levels[i].with_space_around(bottom=20))   
        row_layout.add(hp_button.with_space_around(bottom=20))
        layout.add(row_layout)

    # Create the back button
    back_button = arcade.gui.UIFlatButton(
        text="Back", width=250, style={"font_name": "Melted Monster","bg_color": arcade.color.WHITE,
        "font_color": arcade.color.BLACK}
    )
    back_button.on_click = lambda a:change_views(window, "MenuView")

    layout.add(back_button.with_space_around(top=40,bottom=20))

    

    return arcade.gui.UIAnchorWidget(
        anchor_x="center_x", anchor_y="center_y", child=layout
    )
