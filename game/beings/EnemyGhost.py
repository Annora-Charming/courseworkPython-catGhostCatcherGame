import random
import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class EnemyGhost(pygame.sprite.Sprite):

    def __init__(self):
        super(EnemyGhost, self).__init__()
        self.surf = pygame.Surface((50, 75))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(random.randint(SCREEN_WIDTH-100, SCREEN_WIDTH-20), random.randint(0, SCREEN_HEIGHT-20)))

    def update(self):
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        else:
            self.rect.move_ip(0, +random.randint(-5, 6))