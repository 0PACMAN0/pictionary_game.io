import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
# from main_menu import MainMenu
from menu import Menu
# from tool_bar import ToolBar
from leaderboard import Leaderboard
from player import Player


class Game(object):
    BG = (255, 255, 255)
    COLORS = {
        (255, 255, 255): 0,
        (0, 0, 0): 1,
        (255, 0, 0): 2,
        (0, 255, 0): 3,
        (0, 0, 255): 4,
        (255, 255, 0): 5,
        (255, 140, 0): 6,
        (165, 42, 42): 7,
        (128, 0, 128): 8
    }

    def __init__(self):
        self.HEIGHT = 500
        self.WIDTH = 900
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.leaderboard = Leaderboard(100, 120)
        self.board = Board(300, 120)
        self.top_bar = TopBar(50, 50, 500, 50)
        self.top_bar.change_round(1)

    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)

        pygame.display.update()

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
        pygame.quit()


if __name__ == "__main__":
    pygame.font.init()
    g = Game()
    g.run()
