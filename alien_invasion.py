import sys
import pygame

from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():

    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(ai_settings, screen)
    bullets = pygame.sprite.Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    run_game()




