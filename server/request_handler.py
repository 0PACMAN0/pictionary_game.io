import socket
from player import Player
from game import Game
import threading
import json


class Server(object):
    PLAYERS = 4

    def __init__(self):

        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        """
        player thread handles in communincation
        :param player: 
        :param conn: conn
        :param ip: str
        :param name: str
        :return: None
        """
        while True:
            try:
                try:

                    # send_msg = {}
                    data = conn.recv(1024)
                    data = json.loads(data.decode())
                except Exception as e:
                    break
                keys = [int(key) for key in data.keys()]
                send_msg = {key: [] for key in keys}
                for key in keys:
                    if key == -1:  # get game
                        if player.game:
                            send_msg[-1] = player.game.players
                        else:
                            send_msg[-1] = []

                    if player.game:
                        if key == 0:  # guess
                            correct = player.game.player_guess(player, data[0][0])
                            send_msg[0] = correct
                        elif key == 1:  # skip
                            skip = player.game.skip()
                            send_msg[1] = skip
                        elif key == 2:  # get round
                            content = player.game.round.chat.get_chat()
                            send_msg[2] = content

                        elif key == 3:  # get skip
                            brd = player.game.board.get_board()
                            send_msg[3] = brd
                        elif key == 4:
                            scores = player.game.get_player_scores()
                            send_msg[4] = scores
                        elif key == 5:
                            rnd = player.game.round_count
                            send_msg[5] = rnd
                        elif key == 6:
                            word = player.game.round.word
                            send_msg[6] = word

                        elif key == 7:
                            skips = player.game.round.skips
                            send_msg[7] = skips

                        elif key == 8:
                            x, y, color = data[8][:3]
                            player.game.update_board(x, y, color)
                        elif key == 9:
                            t = player.game.round.time
                            send_msg[9] = t
                        elif key == 10:
                            player.game.board.clear()
                        elif key == 11:
                            send_msg[11] = player.game.round.player_drawing == player

                # if keys
                # for key in
                send_msg = json.dumps(send_msg)
                conn.sendall(send_msg.encode() + ".".encode())

            except Exception() as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected", e)
                break
        if player.game:
            player.game.player_disconnected(player)
        if player in self.connection_queue:
            self.connection_queue.remove(player)
        print(f"[EXCEPTION] {player.get_name()} disconnected")
        conn.close()

    def handle_queue(self, player):
        """
        adds player to queue and creates new game if enough players
        :param player:
        :return:
        """
        self.connection_queue.append(player)
        if len(self.connection_queue) >= 8:
            game = Game(self.game_id, self.connection_queue[:])

            for p in self.connection_queue:
                p.set_game(game)
            self.game_id += 1
            self.connection_queue = []
            print(f"[GAME] Game {self.game_id-1} started...")

    def authentication(self, conn, addr):
        """

        :param addr:
        :param conn:
        :param ip:
        :return:
        """
        try:
            data = conn.recv(1024)
            name = str(data.decode())
            if not name:
                raise Exception("No name received")
            conn.sendall("1".encode())
            player = Player(addr, name)
            self.handle_queue(player)
            thread = threading.Thread(target=self.player_thread, args=(conn, player))
            thread.start()
        except Exception as e:
            print("[EXCEPTION]", e)
            conn.close()

    def connection_thread(self):
        server = "localhost"
        port = 5500
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)

        s.listen(1)
        print("waiting for a connection, server started")

        while True:
            conn, addr = s.accept()
            print("[LOG] new connection! ", addr)
            self.authentication(conn,addr)


if __name__ == "__main__":
    s = Server()
    thread = threading.Thread(target=s.connection_thread)
    thread.start()
