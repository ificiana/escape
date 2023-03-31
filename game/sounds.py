import arcade
import pyglet.media


def change_music(
    player: pyglet.media.Player, to_music: arcade.Sound, looping=False
) -> pyglet.media.Player:
    arcade.stop_sound(player)
    return arcade.play_sound(to_music, looping=looping)
