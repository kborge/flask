from mongoengine import *
import datetime


class AccessCode(Document):
    token = StringField(required=True)
    ip_address = StringField(required=False, default=None)
    mac_address = StringField(required=False, default=None)
    has_expired = BooleanField(default=False)
    browser_used = StringField(required=False, default=None)
    is_activated = BooleanField(default=False)
    refresh_code = StringField(required=False, default=None)
    temporary_code = StringField(required=False, default=None)
    date_modified = DateTimeField(default=datetime.datetime.now)
