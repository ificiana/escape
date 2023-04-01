from game.data.updateDB import updateDB

class data:
    def __init__(self):
        self.db = updateDB("game/data/DB.json")

    def get(self):
        return self.db.get_data()
    
    def unlock_level(self, level:int):
        self.db.unlock_level(level)

    def set_score(self, level:int, score:int):
        self.db.set_score(level, score)