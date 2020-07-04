import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, screen, ai_settings, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.get_bullet_width(), ai_settings.get_bullet_height())
        self.rect.centerx = ship.get_rect().centerx
        self.rect.top = ship.get_rect().top
        self.color = ai_settings.get_bullet_color()
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.get_bullet_speed_factor()

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

