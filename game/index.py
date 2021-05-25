import pygame
from game.beings.Player import Player
from game.beings.EnemyGhost import EnemyGhost
from game.settings import DISPLAY, SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
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

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Ghost Catcher")

farthest_bg = pygame.image.load('images/backgrounds/farthestBack.jpg').convert()
middle_bg = pygame.image.load('images/backgrounds/middleBack.png').convert()

farthest_bg_X = 0
farthest_bg_X2 = farthest_bg.get_width()
middle_bg_X = 0
middle_bg_X2 = middle_bg.get_width()


def redraw_window():
    screen.blit(farthest_bg, (farthest_bg_X, 0))
    screen.blit(farthest_bg, (farthest_bg_X2, 0))
    screen.blit(middle_bg, (middle_bg_X, 400))
    screen.blit(middle_bg, (middle_bg_X2, 400))
    pygame.display.update()


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super(Ground, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, 75))
        self.surf.fill((25, 25, 25))
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 75/2))


player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
new_enemy = EnemyGhost()
enemies.add(new_enemy)
all_sprites.add(new_enemy)
second_enemy = EnemyGhost()
enemies.add(second_enemy)
all_sprites.add(second_enemy)
ground = Ground()
grounds = pygame.sprite.Group()
grounds.add(ground)
all_sprites.add(ground)

running = True

while running:
    redraw_window()
    farthest_bg_X -= 1.4
    farthest_bg_X2 -= 1.4
    middle_bg_X -= 1.4
    middle_bg_X2 -= 1.4

    if farthest_bg_X < farthest_bg.get_width() * -1:
        farthest_bg_X = farthest_bg.get_width()

    if farthest_bg_X2 < farthest_bg.get_width() * -1:
        farthest_bg_X2 = farthest_bg.get_width()

    if middle_bg_X < middle_bg.get_width() * -1:
        middle_bg_X = middle_bg.get_width()

    if middle_bg_X < middle_bg.get_width() * -1:
        middle_bg_X = middle_bg.get_width()

    # player.moving('free')
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            # if event.key == K_LEFT or event.key == K_a:
            #     player.moving('left')
            # if event.key == K_RIGHT or event.key == K_d:
            #     player.moving('right')
            # if event.key == K_UP or event.key == K_w or event.key == K_SPACE:
            #     player.moving('jump')

        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    player.moving(key)
    # player.drawing(screen)
    enemies.update()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        if pygame.sprite.spritecollideany(player, enemies):
            running = False
        if pygame.sprite.spritecollideany(player, grounds):
            Player.isOnGround = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
