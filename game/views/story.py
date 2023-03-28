from typing import Union

import arcade.gui


def get_storybook_ui(
    window: arcade.Window,
) -> Union[arcade.gui.UIWidget, list[arcade.gui.UIWidget]]:
    # Create a vertical BoxGroup to align buttons
    h_box = arcade.gui.UIBoxLayout(vertical=False)

    data = {
        "pages": {
            1: "This is page 1",
            2: "This is page 2",
        },
        "cur_page": 1,
        "max_page": 2,
    }

    text_area = arcade.gui.UITextArea(
        x=100,
        y=200,
        width=200,
        height=300,
        text=data["pages"][data["cur_page"]],
        text_color=arcade.csscolor.WHITE,
    )

    # Create the buttons
    prev_button = arcade.gui.UIFlatButton(text="Prev", width=200)
    h_box.add(prev_button.with_space_around(right=20))

    skip_button = arcade.gui.UIFlatButton(text="Skip", width=200)
    h_box.add(skip_button.with_space_around(right=20))

    next_button = arcade.gui.UIFlatButton(text="Next", width=200)
    h_box.add(next_button.with_space_around(right=20))

    @prev_button.event("on_click")
    def on_click_prev(event):
        print("Prev:", event)
        # TODO: Greyout if cur_page = 1
        data["cur_page"] = max(1, data["cur_page"] - 1)
        text_area.text = data["pages"][data["cur_page"]]

    @next_button.event("on_click")
    def on_click_next(event):
        print("Next:", event)
        # TODO: Start the game after this reaches max_page
        data["cur_page"] = min(data["max_page"], data["cur_page"] + 1)
        text_area.text = data["pages"][data["cur_page"]]

    @skip_button.event("on_click")
    def on_click_skip(event):
        # TODO: Start the game after this
        print("Skip:", event)
        arcade.exit()

    return [
        arcade.gui.UIAnchorWidget(anchor_x="center", anchor_y="bottom", child=h_box),
        text_area,
    ]
