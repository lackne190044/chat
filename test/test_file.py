import pytest
import client

tmp = User('tmp')
tmp2 = User('tmp2')
tmp_group = Group('tmp_group', tmp)
tmp_json = {'name': 'tmp_group', 'owner': 'tmp', 'usernames': [], 'admins': [], 'messages': []}

def test_dummy():
    assert True

def test_send_message():
    try:
        client.user = tmp
        client.send_message()
