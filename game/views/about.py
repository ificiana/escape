import arcade.gui


def get_about_view_ui(window: arcade.Window) -> arcade.gui.UIWidget:
    # Create a vertical BoxGroup to align buttons
    v_box = arcade.gui.UIBoxLayout(vertical=True)
    name_style = {
        "bg_color": arcade.color.BLACK,
        "font_color": arcade.color.WHITE,
        "border_color_pressed": arcade.color.BLACK,
        "font_size": 15,
        "font_name": "Melted Monster",
    }

    names = [
        "Vagish (Vagish Vela)",
        "Tacchan (Arkaprabha Sinha Roy)",
        "Shahnawaz28 (Shahnawaz Hussain)",
        "Arpi369 (Arpita Shaw)",
        "Gods_gift (Veenu Chhabra)",
        "Deb01 (Mainak Deb)",
        "Ryugean (Nayel Abed Razi)",
    ]
    for i in range(3):
        h_box = arcade.gui.UIBoxLayout(vertical=False)
        for j in range(2):
            name = arcade.gui.UIFlatButton(
                text=names[i * 2 + j], width=350, style=name_style
            )
            h_box.add(name)
        v_box.add(h_box)
    name = arcade.gui.UIFlatButton(text=names[-1], width=350, style=name_style)
    v_box.add(name)

    return arcade.gui.UIAnchorWidget(
        anchor_x="center_x", anchor_y="center_y", child=v_box
    )
