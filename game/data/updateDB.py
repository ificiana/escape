import json

class updateDB:
    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        with open(self.filename, "r") as file:
            data = json.load(file)
        return data

    def save_data(self,data):
        with open(self.filename, "w") as file:
            json.dump(data, file)

    def get(self, key):
        data=self.get_data()
        return data[key]
    
    def unlock_level(self, level:int):
        data=self.get_data()        
        data[f"level_{level}"]["is_locked"] = False
        self.save_data(data)

    def set_score(self, level:int, score:int):
        data=self.get_data()   
        data[f"level_{level}"]["high_score"] = score
        self.save_data(data)

"""
# Example usage
db=updateDB("game/data/db.json")
db.get_data()
db.unlock_level(2)
db.set_score(2, 100)
"""