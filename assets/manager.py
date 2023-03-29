import pathlib


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
tilemaps = AssetManager("tilemap")
sounds = AssetManager("sounds")
