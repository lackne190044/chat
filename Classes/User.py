import bcrypt

class User: 
    def __init__(self, username) -> None:
        self._username = username
        self._hashpwd = ''

    def hashpwd(self, password) -> None:
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self._hashpwd = hashed

    def checkpwd(self, password) -> bool:
        return bcrypt.checkpw(password, self._hashpwd)
