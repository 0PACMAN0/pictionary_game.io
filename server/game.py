from .player import Player
from .board import Board
from .round import Round


class Game(object):
    def __init__(self, id, players, thread):
        """
        init the game! once players threshold is met

        :param id:int
        :param players:Player[]

        """
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = Board
        self.player_draw_ind = 0
        self.start_new_round()
        self.create_board()
        self.connected_thread = thread

    def start_new_round(self):
        self.round = Round(self.get_word(), self.players[self.player_draw_ind],self.players,self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()

    def player_guess(self, player, guess):
        """makes the player guess the word

        """
        return self.round.guess(player,guess)

    def player_disconnected(self, player):
        """
        call to clean up objecys player disconnect

        :param player: Player
        :return: Execption()
        """
        pass

    def skip(self):
        """
        ioncrements the roiuns skips are greater theam threshold starts new rounds
        :return: None
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No round statrted yet!")

    def round_ended(self):
        # self.round.skips=0
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):

        self.board.update(x, y, color)

        if not self.board:
            raise Exception("no board created ")
        self.board.update(x, y, color)

    def end_game(self):
        """
        to end the game tha ti s disconect
        :return:
        """

    def get_word(self):
        """
        gives a word that has not yet been used
        :return: str
        """
        # to do get a list of words from someone
        pass
