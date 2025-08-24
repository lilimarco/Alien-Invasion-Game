import pygame.font
from pygame.sprite import Group

from ship import Ship
class Scoreboard():
    def  __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.label_font = pygame.font.SysFont(None, 32) #for the label
        
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
         # Label
        self.score_label = self.label_font.render("Score:", True, self.text_color, self.ai_settings.bg_color)
        self.score_label_rect = self.score_label.get_rect()
        self.score_label_rect.right = self.screen_rect.right - 20
        self.score_label_rect.top = 0 
        #score number
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
        
    def prep_high_score(self):
        # Label
        self.high_score_label = self.label_font.render("High Score:", True, self.text_color, self.ai_settings.bg_color)
        self.high_score_label_rect = self.high_score_label.get_rect()
        self.high_score_label_rect.centerx = self.screen_rect.centerx
        self.high_score_label_rect.top = 0
        #number
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
         # Label
        self.level_label = self.label_font.render("Level:", True, self.text_color, self.ai_settings.bg_color)
        self.level_label_rect = self.level_label.get_rect()
        self.level_label_rect.right = self.screen_rect.right - 20
        self.level_label_rect.top = self.score_rect.bottom + 10
        #number
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 35
        
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
    def show_score(self):
        
        # Draw score + label
        self.screen.blit(self.score_label, self.score_label_rect)
        self.screen.blit(self.score_image, self.score_rect)
        
        # Draw high score + label
        self.screen.blit(self.high_score_label, self.high_score_label_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        
        # Draw level + label
        self.screen.blit(self.level_label, self.level_label_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
        #Draw ships
        self.ships.draw(self.screen)

        