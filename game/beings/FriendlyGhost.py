import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class FriendlyGhost(pygame.sprite.Sprite):

    def __init__(self):
        super(FriendlyGhost, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
