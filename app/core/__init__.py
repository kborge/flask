# register core modules
from app.core.modules.user.methods import method as user


class Modules:
    def __init__(self, mod):
        mod.register_blueprint(user)
