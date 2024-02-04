import random

from board import Board
from round import Round


class Game(object):
    def __init__(self, id, players):
        """
        init the game! once players threshold is met

        :param id:int
        :param players:Player[]

        """
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.round = 1
        self.round_count=0
        self.start_new_round()
        # self.create_board()
        # self.connected_thread = thread

    def start_new_round(self):
        try:
            round_word = self.get_word()
            # self.words_used.append(round_word)
            self.round = Round(self.get_word(), self.players[self.player_draw_ind], self.players, self)
            self.player_draw_ind += 1
            self.round_count += 1
            if self.player_draw_ind >= len(self.players):
                self.round_ended()
                self.end_game()

            self.player_draw_ind+=1
        except Exception as e:
            self.end_game()

    def player_guess(self, player, guess):
        """makes the player guess the word

        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """
        call to clean up objecys player disconnect

        :param player: Player
        :return: Execption()
        """
        if player in self.players:
            player_ind = self.players.index(player)
            if player_ind >= self.player_draw_ind:
                self.player_draw_ind -= 1
            self.players.remove(player)
            self.round.player_left(player)
        else:
            raise Exception("Player not in game ")
        if len(self.players) <= 2:
            self.end_game()

    def get_player_scores(self):
        scores = {player: player.get_score() for player in self.players}
        return scores

    def skip(self):
        """
        ioncrements the roiuns skips are greater theam threshold starts new rounds
        :return: None
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
                return True
            return False
        else:
            raise Exception("No round statrted yet!")

    def round_ended(self):
        # self.round.skips=0
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):

        # self.board.update(x, y, color)

        if not self.board:
            raise Exception("no board created ")
        self.board.update(x, y, color)

    def end_game(self):
        """
        to end the game tha ti s disconect
        :return:
        """
        print(f"[GAME] Game {self.id} ended")
        for player in self.players:
            self.round.player_left(player)

    def get_word(self):
        """
        gives a word that has not yet been used
        :return: str
        """
        # to do get a list of words from someone
        with open("words.txt", "r") as f:
            words = []
            for line in f:
                wrd = line.strip()
                if wrd not in self.words_used:
                    words.append(wrd)
            self.words_used.add(wrd)
            r = random.randint(0, len(words) - 1)
            return words[r].strip()
