import arcade
import pyglet.media


def change_music(
    player: pyglet.media.Player | None,
    to_music: arcade.Sound,
    looping=False,
    speed=1.0,
    volume=1.0,
) -> pyglet.media.Player:
    if player is None:
        player = pyglet.media.Player()
    arcade.stop_sound(player)
    return arcade.play_sound(to_music, looping=looping, speed=speed, volume=volume)
