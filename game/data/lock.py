import os

from game.data.encrypt import SymmetricEncryption
from game.config import SECRET_KEY

print("Get current working directory : ", os.getcwd())
cy = SymmetricEncryption(SECRET_KEY)


# open file in read mode and print its contents
with open(r"game\data\DB.json", "r", encoding="utf8") as file:
    data = file.read()
    encr = cy.encrypt(data)
    print(encr)
    print(cy.decrypt(encr))

with open(r"game\data\DB.json", "w", encoding="utf8") as file:
    file.write(encr.decode("utf-8"))
