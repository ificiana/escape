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
shaders = AssetManager("shaders")


class AudioManager:
    # pylint: disable=R0903
    def __init__(self, sound_folder):
        self.sound_folder = sound_folder
        self.path = AssetManager(sound_folder)

        # declare the sounds
        self.click = arcade.Sound(self.path.resolve("click.wav"))
        self.tomb = arcade.Sound(self.path.resolve("creepy_tomb.wav"))
        self.heart = arcade.Sound(self.path.resolve("cinematic_heartbeat.wav"))
        self.horror = arcade.Sound(self.path.resolve("horror_ambience.wav"))
        self.whoosh = arcade.Sound(self.path.resolve("woosh_hit.wav"))
        # self.glacier = arcade.Sound(self.path.resolve("glacier.mp3"))
        self.japan = arcade.Sound(self.path.resolve("japan.mp3"))
        # self.insomnia = arcade.Sound(self.path.resolve("insomnia.mp3"))


sounds = AudioManager("sounds")
