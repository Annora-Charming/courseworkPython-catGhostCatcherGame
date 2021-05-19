import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.locals import (
    K_UP,
    K_w,
    K_DOWN,
    K_s,
    K_LEFT,
    K_a,
    K_RIGHT,
    K_d
)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(75, 650))

    def moving(self, key):
        # if key[K_UP] or key[K_w]:
            # if self.rect.top < 0:
            #     self.rect.top = 0
            # else:
            #     self.rect.move_ip(0, -1)
        if key[K_LEFT] or key[K_a]:
            if self.rect.left < 0:
                self.rect.left = 0
            else:
                self.rect.move_ip(-5, 0)
        if key[K_RIGHT] or key[K_d]:
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            else:
                self.rect.move_ip(+5, 0)
        # if key[K_DOWN] or key[K_s]:
            # if self.rect.bottom > SCREEN_HEIGHT:
            #     self.rect.bottom = SCREEN_HEIGHT
            # else:
            #     self.rect.move_ip(0, +1)
