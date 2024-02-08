import pygame


class Board(object):
    ROWS = COLS = 720
    COLORS = {
        0: (255, 255, 255),
        1: (0, 0, 0),
        2: (255, 0, 0),
        3: (0, 255, 0),
        4: (0, 0, 255),
        5: (255, 255, 0),
        6: (255, 165, 0),
        7: (165, 42, 42),
        8: (128, 0, 128)

    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 720
        self.width = 720
        self.compressed_board = []
        self.board = self.create_board()

    def create_board(self):
        return [(255, 255, 255) for _ in range(self.COLS) for _ in range(self.ROWS)]

    def translate_board(self):
        # self.board=[self.COLOR[val] for val in /]
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board[y]):
                self.board[y][x] = self.COLORS[col]

    def draw(self, win):
        # pass
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board[y]):
                pygame.draw.rect(win, col, (self.x+x, self.y+y, 1, 1), 0)

    def click(self, x, y):
        row = int(x - self.x)
        col = int(y - self.y)
        if 0 <= row <= self.ROWS and 0 <= col <= self.COLS:
            return (row, col)
        return None

    def update(self, x, y, color):
        self.board[y][x] = color

    def clear(self):
        self.board = self.create_board()
