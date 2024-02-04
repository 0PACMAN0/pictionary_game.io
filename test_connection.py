import socket
import json

import time as t


class Network(object):
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5500
        self.addr = (self.server, self.port)
        self.name = name
        self.connect()
        # self.p =self.connect()

    # def getPlayer(self):
    #     return self.p
    def connect(self):
        try:
            self.client.connect(self.addr)
            # return json.loads(self.client.recv(2048))
            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            print(e)
            # self.client.close()
            self.disconnect(e)

    def send(self, data):

        try:
            data = bytes(data, "utf-8")
            self.client.send(json.dumps(data).encode())
            return json.loads(self.client.recv(2048))
        except socket.error as e:
            # print(e)
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION]dis from server", msg)
        # self.client.shutdown()
        self.client.close()


n = Network("jagan")
print(n.connect())
print(n.send('{0: ""}'))
