from bullet import Bullet
from alien import Alien
import pygame
import sys


def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_RIGHT:
        ship.move_right = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.get_bg_color())

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullet(bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def update_aliens(aliens):
    aliens.update()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.get_bullets_allowed():
        bullet = Bullet(screen, ai_settings, ship)
        bullets.add(bullet)


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_factor
    ai_settings.fleet_direction *= -1


def check_fleet_edges_lf(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges_lf():
            change_fleet_direction(ai_settings, aliens)
            break


def check_fleet_edges_td(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges_td():
            break


def create_fleet(ai_settings, screen, aliens, ship):

    for alien_row in range(get_number_aliens_y(ai_settings, screen, ship.get_rect().height)):
        for alien_number in range(get_number_aliens_x(ai_settings, screen)):
            create_alien(ai_settings, screen, alien_number, alien_row, aliens)


def get_number_aliens_x(ai_settings, screen):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_spacex = ai_settings.get_width() - 2 * alien_width
    number_aliensx = int(available_spacex / (2 * alien_width))
    return number_aliensx


def get_number_aliens_y(ai_settings, screen, ship_height):
    alien = Alien(ai_settings, screen)
    alien_height = alien.rect.height
    available_spacey = ai_settings.get_height() - 3 * alien_height - ship_height
    number_aliensy = int(available_spacey / (2 * alien_height))
    return number_aliensy


def create_alien(ai_settings, screen, alien_number, alien_row, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * alien_row
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)
