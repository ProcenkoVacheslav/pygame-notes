import pygame
from settings import *
from colors import *

class EnterField:
    def __init__(self, x=0, y=0, width=100, height=40, color=white, field=None, text='', text_color=blask, len=15, word_size=10, run_opportunity=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.field = field
        self.color = color
        self.main_color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, word_size)
        self.txt_surface = self.font.render(text, True, self.text_color)
        self.active = False
        self.main_text = text
        self.text = text
        self.words_len = len
        self.unective_color = color
        self.run_opportunity = run_opportunity
        self.active_color = color
        self.text_y = self.rect.y
        self.word_size = word_size

    def color(self, new_color):
        self.color = new_color

    def draw(self, border=0, border_color=blask, shift_x=5, shift_y=1, rect_widht=0, shape=0, active_color=orange, unective_color=white):
        self.active_color = active_color
        self.unective_color = unective_color
        pygame.draw.rect(self.field, self.color, self.rect, rect_widht, shape)
        if border > 0:
            pygame.draw.rect(self.field, border_color, self.rect, border, shape)
        self.field.blit(self.txt_surface, (self.rect.x + shift_x, self.text_y + shift_y))

    def colidpoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def guidens(self, x, y):
        if self.rect.collidepoint(x, y):
            self.color = self.active_color
        else:
            self.color = self.main_color

    def return_text(self):
        return self.text

    def run(self, run_opportunity=True):
        self.run_opportunity = run_opportunity

    def change_text(self, text):
        self.text = text
        self.txt_surface = self.font.render(self.text, True, self.text_color)

    def handle_event(self, event, function, content, second_function=0):
        if self.run_opportunity:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = self.active_color if self.active else self.unective_color
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        function(content)
                        if second_function != 0:
                            second_function()
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        if len(self.text) < self.words_len:
                            self.text += event.unicode
                    self.txt_surface = self.font.render(self.text, True, self.text_color)