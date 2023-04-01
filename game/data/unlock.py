from encrypt import SymmetricEncryption
from game.config import SECRET_KEY   

data=None
cy=SymmetricEncryption(SECRET_KEY)

# open file in read mode and print its contents
with open("game\data\DB.json", 'r') as file:
    data=file.read()
    data=data.encode('utf-8')
    print(data)
    decr=cy.decrypt(data)
    print(decr)

with open("game\data\DB.json", 'w') as file:
    decr.replace("=",":")
    file.write(decr)
