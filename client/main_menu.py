import pygame
from network import Network
from game import Game


# pygame.font.init()

class MainMenu:
    BG = (255, 255, 255)

    def __init__(self):
        self.HEIGHT = 800
        self.WIDTH = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.name = ""
        self.waiting = False
        self.name_font = pygame.font.SysFont("comicsans", 80)
        self.title_font = pygame.font.SysFont("comicsans", 120)
        self.enter_font = pygame.font.SysFont("comicsans", 120)

    def draw(self):
        self.win.fill(self.BG)
        title = self.title_font.render("Pictonary!", 1, (0, 0, 0))
        self.win.blit(title, (self.WIDTH / 2 - title.get_width() / 2, 50))
        name = self.name_font.render("Type a Name:" + self.name, 1, (0, 0, 0))
        self.win.blit(name, (100, 400))

        if self.waiting:
            enter = self.enter_font.render("Press enter to join the game....", 1, (0, 0, 0))
            self.win.blit(enter, (self.WIDTH / 2 - title.get_width() / 2, 800))
        else:
            enter = self.enter_font.render("Press enter to join the game....", 1, (0, 0, 0))
            self.win.blit(enter, (self.WIDTH / 2 - title.get_width() / 2, 800))

        pygame.display.update()

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            self.draw()
            if self.waiting:
                response = self.n.send({-1: []})

                if response:
                    pygame.quit()
                    run = False
                    g = Game(self.win,self.n)
                    g.players.append()
                    g.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    # run = False
                    if event.key == pygame.K_RETURN:
                        if len(self.name) > 1:
                            run = False
                            self.waiting = True
                            self.n = Network(self.name)
                            # response = n.send({-1:[]})
                    else:
                        key_name = pygame.key.name(event.key)
                        key_name = key_name.upper()
                        self.type(key_name)

    def type(self, char):
        if char == "BACKSPACE":
            if len(self.name) > 0:
                self.name = self.name[:-1]
            elif char == "SPACE":
                self.name += " "

            elif len(char) == 1:

                self.name += char

            if len(self.name) >= 25:
                self.name = self.name[:25]


if __name__ == "__main__":
    pygame.font.init()
    main = MainMenu()
    main.run()
