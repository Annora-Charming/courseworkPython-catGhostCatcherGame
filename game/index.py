import pygame
from game.beings.Player import Player
from game.beings.EnemyGhost import EnemyGhost
from game.settings import DISPLAY
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN
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

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    player.moving(key)
    player.drawing(screen)
    enemies.update()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        if pygame.sprite.spritecollideany(player, enemies):
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
