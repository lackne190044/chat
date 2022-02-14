import bcrypt
from getpass import getpass

master_secret_key = getpass('tell me the master secret key you are going to use')

salt = bcrypt.gensalt()

combo_password = raw_password + salt + master_secret_key
hashed_password = bcrypt.hashpw(combo_password, salt)
print(hashed_password)