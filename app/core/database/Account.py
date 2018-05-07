from mongoengine import *
from app.core.database.User import User as UserModel
from app.core.database.Access_Code import AccessCode
from app.core.database.extensions.status import Status

import datetime


class Account(Document):
    User = ReferenceField(UserModel, dbref=True)
    Access_Code = ReferenceField(AccessCode, dbref=True)
    is_email_verified = BooleanField(default=False)
    is_account_verified = BooleanField(default=False)
    token_verification = StringField(default=None)
    status = ListField(StringField(
        default=Status().default, choices=Status().all), default=Status().default)
    date_modified = DateTimeField(default=datetime.datetime.now())

