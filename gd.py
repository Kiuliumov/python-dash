from config import Config

class Client:
    BASE_URL = "http://www.boomlings.com/database/"

    def __init__(self, game_version=22, binary_version=35, gdw=0, secret=None):
        config = Config()
        self.game_version = game_version
        self.binary_version = binary_version
        self.gdw = gdw
        self.secret = secret if secret is not None else config.secret

    @property
    def game_version(self):
        return self.__game_version

    @game_version.setter
    def game_version(self, game_version):
        if not isinstance(game_version, int):
            raise TypeError("game_version must be an integer")
        if game_version < 10:
            raise ValueError("game_version must be at least 10")

        self.__game_version = game_version
