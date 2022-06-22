"""For all interactions with groups"""
from Classes.Group import Group
from Classes.User import User
from Classes.Message import Message
from Classes.CustomError import CustomError
import json
import os

class GroupCommandHandler:
    """Create the class"""
    def __init__(self, group: Group = None, commandingUser: User = None):
        """Initialize the class"""
        self._commanding_user = commandingUser
        if type(self._commanding_user) != str and self._commanding_user != None:
            self._commanding_user = self._commanding_user
        self._group = group
        if self._commanding_user is not None and self._group is not None:
            if commandingUser._username not in self._group._usernames and commandingUser._username != self._group._owner:
                raise CustomError('Commanding User not in group')

    def load_messages(self):
        """Load all messages from the group"""
        to_return = ''
        for i in self._group._messages:
            to_return += f'{i["user"]} | {i["date"]}\n'
            to_return += f'{i["text"]}\n\n'
        return to_return

    @property
    def is_admin(self):
        """Check if _commanding_user is an admin"""
        if self._commanding_user in self._group._admins or self._commanding_user._username == self._group._owner:
            return True
        return False

    def user_in_group(self, user):
        """Check if user is in group"""
        if user._username in self._group._usernames or user._username == self._group._owner:
            return True
        return False

    def needs_admin_error(self):
        """Check if _commanding_user is an admin and return error message if not"""
        if not self.is_admin:
            print('Commanding user is not admin.')
            return False
        return True

    def add_user(self, user):
        """Add a user to the group"""
        if not self.needs_admin_error(): 
            return
        if self.user_in_group(user):
            print('User already in Group.')
            return
        self._group.addUser(user)

    def remove_user(self, user):
        """Remove a user from the group"""
        if not self.needs_admin_error:
           return
        if not self.user_in_group(user):
           print('User is not in group.') 
           return
        self._group.removeUser(user)

    def add_admin(self, user):
        """Promote a user to admin"""
        if not self.needs_admin_error():
            return
        if not self.user_in_group(user):
            print('User is not in group.')
            return
        self._group.addAdmin(user)

    def remove_admin(self, user):
        """Demote a admin to user"""
        if not self.needs_admin_error():
            return
        if not self.user_in_group(user):
            print('User is not in group.')
            return
        self._group.removeAdmin(user)

    def get_group(self):
        """Return the group"""
        return self._group

    def add_message(self, message: Message):
        """Add a message to the group"""
        self._group.addMessage(Message(self._commanding_user ,message))

    def save(self):
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'Groups', self._group._name + '.json')
        with open(file_path, 'w') as _file:
            json.dump(self.json, _file, indent=3)

    def load(self, file):
        """Load a group from a file"""
        self.__init__(commandingUser=self._commanding_user)
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'Groups', file)

        with open(file_path, 'r') as _file:
            _data = json.load(_file)
            _group = Group(_data['name'], User(_data['owner']))
            for i in _data['usernames']:
                _group.addUser(User(i))
            for i in _data['admins']:
                _group.addAdmin(i)
            for i in _data['messages']:
                msg =Message(User(i['user']), i['text'], i['date'])
                _group.addMessage(msg)
        self._group = _group

    @property
    def json(self):
        """Return a json string of the group"""
        return self._group.json
