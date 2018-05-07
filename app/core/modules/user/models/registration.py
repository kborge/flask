from app.core.database.User import User
from mongoengine import ValidationError
from app.config.config import JWT_SECRET_KEY, JWT_HASH
import bcrypt
import validators
import json
import jwt


class Registration:

    def __init__(self, first_name, last_name, email, **kwargs):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        for key, value in kwargs.items():
            if key == 'email' or key == 'first_name' or key == 'last_name':
                raise KeyError('{} cannot be custom define.'.format(key))
            setattr(self, key, value)

    def __call__(self):
        try:
            if self.__validate_email(self.email) is True:
                if self.__check_account_availability(self.email) is True:
                    try:
                        db_result = self.__store_to_database(self.__dict__)
                        if isinstance(db_result, (dict, list)):
                            return db_result
                        else:
                            raise TypeError('Not a JSON format.')
                    except KeyError as error:
                        raise KeyError(str(error))
                else:
                    raise LookupError('Account already taken.')
            else:
                raise ValueError('Invalid email format.')
        except KeyError as error:
            raise KeyError(str(error))

    @staticmethod
    def __validate_email(email):
        if validators.email(email):
            return True
        return False

    @staticmethod
    def __check_account_availability(email):
        if User.objects(email=email, deleted_at=None).count() is not 0:
            return False
        return True

    @staticmethod
    def __store_to_database(dictionary):
        try:
            user = User()
            for key, value in dictionary.items():
                if key == 'password' and isinstance(key, str):
                    if len(value) >= 8:
                        value = (bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt())).decode('utf-8')
                    else:
                        raise ValueError('Password string length must be 8 and above.')
                setattr(user, key, value)
            user.save()
            user = json.loads(user.to_json())
            user['id'] = user['_id']['$oid']
            del user['_id']
            user['access_token'] = jwt.encode(user, JWT_SECRET_KEY, algorithm=JWT_HASH).decode('utf-8')
            return user
        except ValidationError as error:
            raise KeyError(str(error))
