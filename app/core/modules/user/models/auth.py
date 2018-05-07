from app.core.database.User import User
from app.config.config import JWT_SECRET_KEY, JWT_HASH
from mongoengine import DoesNotExist
import json
import bcrypt
import jwt
import validators


class Auth:
    email = None
    password = None
    # import pdb; pdb.set_trace()

    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.password = password

    def __call__(self):
        try:
            if self.__validate_email():
                return self.__database_lookup()
            else:
                raise KeyError('Invalid email format.')
        except (ValueError, LookupError, KeyError) as error:
            raise ValueError(str(error)) or LookupError(str(error)) or KeyError(str(error))

    def __validate_email(self):
        if not validators.email(self.email):
            return False
        return True

    def __database_lookup(self):
        try:
            user = User.objects.get(email=self.email, deleted_at=None)
            if not user.password:
                raise LookupError('Invalid account')
            elif self.__validate_password(password=self.password, account_password=user.password):
                acc_json = json.loads(user.to_json())
                acc_json['access_token'] = jwt.encode(acc_json, JWT_SECRET_KEY, algorithm=JWT_HASH).decode('utf-8')
                acc_json['id'] = acc_json['_id']['$oid']
                del acc_json['_id']
                del acc_json['password']
                del acc_json['date_modified']
                return acc_json
            else:
                raise LookupError("Invalid password.")
        except DoesNotExist:
            raise LookupError('Invalid account')

    @staticmethod
    def __validate_password(password, account_password):
        if bcrypt.checkpw(password.encode('utf-8'), account_password.encode('utf-8')):
            return True
        else:
            return False
