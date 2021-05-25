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
    K_d,
    K_SPACE
)


class Player(pygame.sprite.Sprite):
    isOnGround = False
    # walking = False
    # walkingCycle = [pygame.image.load('images/player/walk/Walk (1).png'),
    #                 pygame.image.load('images/player/walk/Walk (2).png'),
    #                 pygame.image.load('images/player/walk/Walk (3).png'),
    #                 pygame.image.load('images/player/walk/Walk (4).png'),
    #                 pygame.image.load('images/player/walk/Walk (5).png'),
    #                 pygame.image.load('images/player/walk/Walk (6).png'),
    #                 pygame.image.load('images/player/walk/Walk (7).png'),
    #                 pygame.image.load('images/player/walk/Walk (8).png'),
    #                 pygame.image.load('images/player/walk/Walk (9).png'),
    #                 pygame.image.load('images/player/walk/Walk (10).png')]
    # jumpingCycle = [pygame.image.load('images/player/jump/Jump (1).png'),
    #                 pygame.image.load('images/player/jump/Jump (2).png'),
    #                 pygame.image.load('images/player/jump/Jump (3).png'),
    #                 pygame.image.load('images/player/jump/Jump (4).png'),
    #                 pygame.image.load('images/player/jump/Jump (5).png'),
    #                 pygame.image.load('images/player/jump/Jump (6).png'),
    #                 pygame.image.load('images/player/jump/Jump (7).png'),
    #                 pygame.image.load('images/player/jump/Jump (8).png')]
    # idleCycle = [pygame.image.load('images/player/idle/Idle (1).png'),
    #              pygame.image.load('images/player/idle/Idle (2).png'),
    #              pygame.image.load('images/player/idle/Idle (3).png'),
    #              pygame.image.load('images/player/idle/Idle (4).png'),
    #              pygame.image.load('images/player/idle/Idle (5).png'),
    #              pygame.image.load('images/player/idle/Idle (6).png'),
    #              pygame.image.load('images/player/idle/Idle (7).png'),
    #              pygame.image.load('images/player/idle/Idle (8).png'),
    #              pygame.image.load('images/player/idle/Idle (9).png'),
    #              pygame.image.load('images/player/idle/Idle (10).png')]
    # animationCount = 0

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(75, 0))
        self.speed = 5
        self.jumpProcess = 10

    def moving(self, key):
        if not Player.isOnGround:
            self.rect.move_ip(0, +self.speed)
        if key[K_LEFT] or key[K_a]:
            Player.walking = True
            if self.rect.left < 0:
                self.rect.left = 0
            else:
                self.rect.move_ip(-self.speed, 0)
        if key[K_RIGHT] or key[K_d]:
            Player.walking = True
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            else:
                self.rect.move_ip(+self.speed, 0)
        if key[K_SPACE] or key[K_UP] or [K_w]:
            if Player.isOnGround:
                # Player.walking = False
                if self.jumpProcess >= -10:
                    if self.jumpProcess > 0:
                        self.rect.move_ip(0, -(self.jumpProcess ** 2) / 2)
                    else:
                        self.rect.move_ip(0, (self.jumpProcess ** 2) / 2)
                    self.jumpProcess -= 1
                else:
                    self.jumpProcess = 10

    # def moving(self, move_type):
    #     if not Player.isOnGround:
    #         self.rect.move_ip(0, +self.speed)
    #     if move_type == 'left':
    #         # Player.walking = True
    #         if self.rect.left < 0:
    #             self.rect.left = 0
    #         else:
    #             self.rect.move_ip(-self.speed, 0)
    #     if move_type == 'right':
    #         # Player.walking = True
    #         if self.rect.right > SCREEN_WIDTH:
    #             self.rect.right = SCREEN_WIDTH
    #         else:
    #             self.rect.move_ip(+self.speed, 0)
    #     if Player.isOnGround and move_type == 'jump':
    #         # Player.walking = False
    #         #self.isJumping = True
    #         #if self.isJumping:
    #         if self.jumpProcess >= -10:
    #             if self.jumpProcess > 0:
    #                 self.rect.move_ip(0, -(self.jumpProcess ** 2) / 2)
    #             else:
    #                 self.rect.move_ip(0, (self.jumpProcess ** 2) / 2)
    #             self.jumpProcess -= 1
    #         else:
    #             Player.isOnGround = False
    #             self.jumpProcess = 10

    def jumping(self, key):
        pass

    # def drawing(self, window):
    #     if Player.animationCount + 1 >= 60:
    #         Player.animationCount = 0
    #     if Player.walking:
    #         window.blit(Player.walkingCycle[Player.animationCount // 5], (self.rect.x, self.rect.y))
    #         Player.animationCount += 1
    #     elif self.isJumping:
    #         window.blit(Player.jumpingCycle[Player.animationCount // 5], (self.rect.x, self.rect.y))
    #         Player.animationCount += 1
    #     else:
    #         window.blit(Player.idleCycle[Player.animationCount // 5], (self.rect.x, self.rect.y))
    #         Player.animationCount += 1
