from CommandHandlers.GroupCommandHandler import GroupCommandHandler
from Classes.User import User
from Classes.Group import Group

tmp = User('tmp')
tmp2 = User('tmp2')
tmp_group = Group('tmp_group', tmp)
tmp_json = {'name': 'tmp_group', 'owner': 'tmp', 'usernames': [], 'admins': [], 'messages': []}

def test_dummy():
    assert True

def test_init():
    GCH = GroupCommandHandler(tmp_group, tmp)
    assert GCH._commanding_user == tmp
    assert GCH._group == tmp_group

def test_load():
    GCH = GroupCommandHandler(commandingUser=tmp)
    GCH.load('tmpGroup.json')
    assert GCH._group._owner == tmp._username

def test_json():
    GCH = GroupCommandHandler(tmp_group, tmp)
    assert GCH.json == tmp_json

def test_adduser():
    _json = tmp_json
    _json['usernames'] = [ 'tmp2' ]
    GCH = GroupCommandHandler(tmp_group, tmp)
    GCH.add_user(tmp2)
    assert GCH.json == _json

def test_is_admin():
    test = tmp_group
    GCH = GroupCommandHandler(tmp_group, tmp)
    GCH.add_user(tmp2)
    test = GCH.get_group()
    assert GCH.is_admin
    GCH = GroupCommandHandler(test, tmp2)
    assert not GCH.is_admin
