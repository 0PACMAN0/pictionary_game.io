import pygame


class Button(object):
    def __init__(self, x, y, width, height, color, border_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.border_color = border_color
        self.BORDER_WIDTH = 2

    def draw(self, win):
        pygame.draw.rect(win, self.border_color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(win, self.border_color, (
            self.x + self.BORDER_WIDTH, self.y + self.BORDER_WIDTH, self.width - self.BORDER_WIDTH * 2,
            self.height - self.BORDER_WIDTH * 2), 0)

    def click(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True

        return False


class TextButton(Button):
    def __init__(self, x, y, width, height, text, color, border_color=(0, 0, 0)):
        super().__init__(x, y, width, height, color, border_color)
        self.text = text


