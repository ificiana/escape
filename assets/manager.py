import pathlib

import arcade


class AssetManager:
    def __init__(self, root):
        self._root = pathlib.Path("assets").joinpath(root)

    def resolve(self, file):
        return str(self._root.joinpath(file))

    def get_absolute_path(self, file):
        return str(self._root.joinpath(file).absolute())

    def get_resolved_path(self, file):
        return str(self._root.joinpath(file).absolute().resolve())


sprites = AssetManager("sprites")
tilemaps = AssetManager("tilemaps")
fonts = AssetManager("fonts")
items = AssetManager("items")


class AudioManager:
    # pylint: disable=R0903
    def __init__(self, sound_folder):
        self.sound_folder = sound_folder
        self.path = AssetManager(sound_folder)

        # declare the sounds
        self.click = arcade.Sound(self.path.resolve("click.wav"))
        self.bg1 = arcade.Sound(self.path.resolve("creepy_tomb.wav"))
        self.bg2 = arcade.Sound(self.path.resolve("cinematic_heartbeat.wav"))


sounds = AudioManager("sounds")
