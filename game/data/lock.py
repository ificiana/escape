from encrypt import SymmetricEncryption
from game.config import SECRET_KEY   

import os
print('Get current working directory : ', os.getcwd())
data=None
cy=SymmetricEncryption(SECRET_KEY)


# open file in read mode and print its contents
with open("game\data\DB.json", 'r') as file:
    data=file.read()
    encr=cy.encrypt(data)
    print(encr)
    print(cy.decrypt(encr))

with open("game\data\DB.json", 'w') as file:
    file.write(encr.decode('utf-8'))

