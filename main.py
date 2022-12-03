import pygame
import config
import game


pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
g = game.Game(screen)
g.run()
pygame.quit()
