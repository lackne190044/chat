import bcrypt
import json
import os

class User: 
    """Class representing a User."""
    def __init__(self, username) -> None:
        """Initialize the user."""
        self._username = username
        self._hashpwd = ''

    def read_file(self):
        """Search for the user in the users file and get the hashed password."""
        current_dir = os.getcwd()
        with open(f'{current_dir}/users.json') as file:
            data = json.load(file)
            for i in data:
                if i['username'] == self._username:
                    self._hashpwd = i['password']

    def hashpwd(self, password) -> None:
        """Hash and save the password of a user."""
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self._hashpwd = hashed

    def checkpwd(self, password) -> bool:
        """Check if the password is correct."""
        password = password
        return bcrypt.checkpw(password.encode('utf-8'), self._hashpwd.encode('utf-8'))
