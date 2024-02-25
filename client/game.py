import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from main_menu import MainMenu

# from tool_bar import ToolBar
from leaderboard import Leaderboard
from player import Player
from bottom_bar import BottomBar


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
        self.HEIGHT = 800
        self.WIDTH = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.leaderboard = Leaderboard(50, 120)
        self.board = Board(300, 120)
        self.top_bar = TopBar(10, 10, 800, 100)
        self.top_bar.change_round(1)
        self.players = [Player("Tim"), Player("Timu"), Player("Timi"), Player("Time"), Player("Tiem")]
        self.skip_button = TextButton(200, 800, 100, 50, (255, 255, 0), "SKIP")
        self.bottom_bar = BottomBar(10, 810,self)
        self.chat = Chat(1000, 125)
        self.draw_color = (0, 0, 0)
        for player in self.players:
            self.leaderboard.add_player(player)

    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        self.skip_button.draw(self.win)
        self.chat.draw()
        pygame.display.update()

    def check_clicks(self):
        """
        handles clicks
        :return:
        """
        mouse = pygame.mouse.get_pos()
        if self.skip_button.click(*mouse):
            print("skipped")
        clicked_board = self.board.click(*mouse)
        if clicked_board:
            self.board.update(*clicked_board, (0, 0, 0))

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
                if pygame.mouse.get_pressed()[0]:
                    self.check_clicks()
        pygame.quit()


if __name__ == "__main__":
    pygame.font.init()
    g = Game()
    g.run()
