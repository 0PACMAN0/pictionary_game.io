import time as t
# from _thread import *
# from game import Game
from _thread import *
from chat import Chat


class Round(object):
    def __init__(self, word, player_drawing, game):
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0

        self.time = 75
        self.game = game
        self.chat = Chat(self)
        # self.players = players
        self.player_scores = {player: 0 for player in game.players}
        # self.start=time.time()
        """
        check the lline above
        """
        start_new_thread(self.time_thread, ())

    def skip(self):
        self.skips += 1
        if self.skips > len(self.game.players) - 2:
            self.skips = 0
            return True
        return False

    def get_scores(self):
        """return all players score"""
        return self.player_scores

    def get_score(self, players):
        if players in self.player_scores:
            return self.player_scores[players]
        else:
            raise Exception("Player not in score list ")

    def time_thread(self):
        """
        runs in thread to keep track of time

        :return:None
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1

        self.end_round(" Time is up ")

    def guess(self, player, wrd):
        """
        :return bool if player got it right
        :param player:
        :param wrd:
        :return:
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
            self.chat.update_chat(f"{player.name} has guessed {wrd}")
            return True
        self.chat.update_chat(f"{player.name} guessed {wrd}")
        return False

    def player_left(self, player):
        """

        :param player:Player
        :return: None
        """
        if player in self.player_scores:
            del self.player_scores[player]
        if player in self.player_guessed:
            self.player_guessed.remove(player)
        if player == self.player_drawing:
            self.chat.update_chat(f"round has been skipped because the drawer left. ")
            self.end_round(" drawing player leaves ")

    def end_round(self):
        for player in self.game.players:
            if player in self.player_scores:
                player.update_score(self.player_scores[player])
            # else:

        self.game.round_ended()
