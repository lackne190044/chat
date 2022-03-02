from Classes.Group import Group
from Classes.User import User
from Classes.Message import Message
from Classes.CustomError import CustomError
import json

class GroupCommandHandler:
    def __init__(self, group: Group = None, commandingUser: User = None):
        self._commanding_user = commandingUser
        self._group = group
        if self._commanding_user is not None and self._group is not None:
            if commandingUser._username not in self._group._usernames and commandingUser._username is not self._group._owner:
                print(commandingUser._username)  
                for i in self._group._usernames:
                    print(i)
                raise CustomError('Commanding User not in group')

    @property
    def is_admin(self):
        if self._commanding_user._username in self._group._admins or self._commanding_user._username == self._group._owner:
            return True
        return False

    def user_in_group(self, user):
        if user._username in self._group._usernames or user._username == self._group._owner:
            return True
        return False

    def needs_admin_error(self):
        if not self.is_admin:
            print('Commanding user is not admin.')
            return False
        return True

    def add_user(self, user):
        if not self.needs_admin_error(): 
            return
        if self.user_in_group(user):
            print('User already in Group.')
            return
        self._group.addUser(user)

    def remove_user(self, user):
        if not self.needs_admin_error:
           return
        if not self.user_in_group(user):
           print('User is not in group.') 
           return
        self._group.removeUser(user)

    def add_admin(self, user):
        if not self.needs_admin_error():
            return
        if not self.user_in_group(user):
            print('User is not in group.')
            return
        self._group.addAdmin(user)

    def remove_admin(self, user):
        if not self.needs_admin_error():
            return
        if not self.user_in_group(user):
            print('User is not in group.')
            return
        self._group.removeAdmin(user)

    def get_group(self):
        return self._group

    def add_message(self, message: Message):
        if self._commanding_user._username != message._username:
            print('message doesnt belong to user')
            return
        self._group.addMessage(message)

    def load(self, file):
        with open(file, 'r') as _file:
            _data = json.load(_file)
            _group = Group(_data['name'], User(_data['owner']))
            for i in _data['usernames']:
                _group.addUser(User(i))
            for i in _data['admins']:
                _group.addAdmin(User(i))
            for i in _data['messages']:
                msg =Message(User(i['user']), i['text'], i['date'])
                _group.addMessage(msg)
        self._group = _group

    @property
    def json(self):
        return self._group.getJson()
