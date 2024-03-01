import socket
import json

import time as t


class Network(object):
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5556
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

    def send_str(self, data):
        try:
            self.client.connect(self.addr)
            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)

    def send(self, data):

        try:
            # data = bytes(data, "utf-8")
            # self.client.connect(self.addr)
            self.client.send(json.dumps(data).encode())
            d = ""
            while 1:
                last = self.client.recv(1024).decode()
                d += last
                try:
                    if d.count(".") == 1:
                        break
                except:
                    pass
                try:
                    if d[-1] == ".":
                        d = d[:-1]
                except:
                    pass

                keys = [key for key in data.keys()]
                return json.loads(d)(str(keys[0]))
        except socket.error as e:
            # print(e)
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION]disconnected from server", msg)

        self.client.close()

