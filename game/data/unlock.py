from game.data.encrypt import SymmetricEncryption
from game.config import SECRET_KEY

cy = SymmetricEncryption(SECRET_KEY)

# open file in read mode and print its contents
with open(r"game\data\DB.json", "r", encoding="utf8") as file:
    data = file.read()
    data = data.encode("utf-8")
    print(data)
    decr = cy.decrypt(data)
    print(decr)

with open(r"game\data\DB.json", "w", encoding="utf8") as file:
    decr.replace("=", ":")
    file.write(decr)
