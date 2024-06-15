import pygame
from colors import *

class Bottomn:
    def __init__(self, x=0, y=0, width=100, height=40, color=white, border_color=blask, field=None, font=None):
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.color = color
        self.main_color = color
        self.border_color = border_color
        self.main_border_color = border_color
        self.win = field
        self.run_opportunity = False
        self.event = pygame.event.get()
        self.font = font

    def color(self, new_color):
        self.color = new_color

    def set_text(self, text=' ', fsize=1, text_color=blask):
        self.text = text
        self.image = pygame.font.Font(self.font, fsize).render(self.text, True, text_color)

    def draw(self, border=0, shift_x=0, shift_y=0, rect_widht=0, shape=0, new_x=-1, new_y=-1):
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(self.win, self.color, self.rect, rect_widht, shape)
        if border > 0:
            pygame.draw.rect(self.win, self.border_color, self.rect, border, shape)
        self.win.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def colidpoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def guidens(self, x, y, guid_color=yellow, border_color=blask):
        if self.rect.collidepoint(x, y):
            self.color = guid_color
            self.border_color = border_color
        else:
            self.color = self.main_color
            self.border_color = self.main_border_color

    def run(self, run_opportunity=True):
        self.run_opportunity = run_opportunity

    def return_text(self):
        return self.text

    def click(self, click, function, pos_x, pos_y, content=0, second_function=None):
        if self.run_opportunity:
            if click.type == pygame.MOUSEBUTTONDOWN and click.button == 1:
                if self.rect.collidepoint(pos_x, pos_y):
                    function(content)
                    if second_function != None:
                        second_function()