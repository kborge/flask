import datetime
from mongoengine import *


class User(Document):
    avatar = StringField(default="https://ca.slack-edge.com/T18L7SU9J-U1947DMQX-1cb581685ea7-512")
    email = EmailField(required=True)
    password = StringField(reuired=True)
    first_name = StringField(required=True, max_length=20)
    middle_name = StringField(default=None, max_length=20)
    last_name = StringField(required=True, max_length=20)
    contact_number = StringField(default=None)
    title = StringField(default='Mr', choices=['Ms', 'Mr', 'Mrs'])
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    deleted_at = DateTimeField(required=False)
    date_modified = DateTimeField(default=datetime.datetime.now())

