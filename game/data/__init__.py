from game.data.update_db import UpdateDB


class Data:
    def __init__(self):
        self.db = UpdateDB("game/data/DB.json")

    def get(self):
        return self.db.get_data()

    def unlock_level(self, level: int):
        self.db.unlock_level(level)

    def set_score(self, level: int, score: int):
        self.db.set_score(level, score)
