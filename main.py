import arcade
from config import *


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)


def main():
    Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Game")
    arcade.run()
