from game import Game


class Player(object):
    def __init__(self, ip, name):
        """
        init player object

        :param ip:str         :param name:str

        """
        self.game = None

        self.ip = ip
        self.name = name
        self.score = 0

    def set_game(self, game):
        """
        sets the player game association

        :return:None

        """
        self.game = game

    def update_score(self, x):
        self.score += x

    def guess(self, wrd):
        return self.game.player_guess(self, wrd)

    def disconnect(self):
        """
        call to disconnect player
        requires execution
        :return:None
        """
        self.game.player_disconnected(self)

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def get_ip(self):
        """
        get player ip address

        :return:str
        """
        return self.ip
