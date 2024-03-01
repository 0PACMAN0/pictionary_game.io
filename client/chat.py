import pygame


class Chat(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 900
        self.BORDER_THICKNESS = 5
        self.content = []
        self.typing = ""
        self.chat_font = pygame.font.SysFont("comicsans", 15)
        # self.chat = Chat(1000,)
        self.CHATGAP = 5

    def update_chat(self, msg):
        # self.content.append(msg)

        self.content=self.content[:-1]
    def draw(self, win):
        pygame.draw.rect(win, (221, 220, 220), (self.x, self.y + self.height - 100, self.width, 100),
                         self.BORDER_THICKNESS)
        pygame.draw.line(win,(0,0,0),(self.x,self.y +selfheight - 40),(self.x+self.width,self.y +self.height-40),self.BORDER_THICKNESS)
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), self.BORDER_THICKNESS)
        while len(self.content) * self.CHATGAP > self.height - 100:
            # chat = chat[:-1]
        for i, chat in enumerate(self.content):
            txt = self.chat_font.render(chat, 1, (0, 0, 0))
            win.blit(txt, self.x + 5, self.y + i * self.CHATGAP)

        type_chat = self.chat_font.render(self.typing ,1,(0,0,0))
        win.blit(type_chat,(self.x+5,self.y+50 - type_chat.get_height()/2))

    def type(self, char, delete=False):
        if char == "BACKSPACE":
            if len(self.typing)>0:
                self.typing = self.typing[:-1]
            elif char == "SPACE":
                self.typing += " "

            elif len(char)==1:

                self.typing += char

            if len(self.typing)>=25:
                self.typing = self.typing[:25]

