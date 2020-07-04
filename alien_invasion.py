import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf
import time


def run_game():
    pygame.init()
    ai_settings = Settings()
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.get_width(), ai_settings.get_height()))
    # print(dir(screen.get_rect()))
    ship = Ship(screen, ai_settings)
    alien = Alien(ai_settings, screen)
    # print("(x=%d, y=%d)" %(ship.get_rect().x, ship.get_rect().y))
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullet(bullets, aliens)
        gf.update_aliens(aliens)
        gf.check_fleet_edges_td(ai_settings, aliens)
        gf.check_fleet_edges_lf(ai_settings, aliens)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        # time.sleep(0.1)


run_game()