import pygame
pygame.font.init()

FPS = 24
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

MU = 0.4 #соотношение между шириной окна и стороной поля

SIDE = int(MU * SCREEN_WIDTH)
IDENT = int((SCREEN_WIDTH - 2 * SIDE)/3)
FIELD_SIZE = (SIDE, SIDE)
FIELDS_POS = ((IDENT, IDENT), (IDENT * 2 + SIDE, IDENT))
GRID = int(FIELD_SIZE[0]//10)

NU = 0.6 #соотношение между стороной клетки и размером шрифта
FONT_AXIS_SIZE = int(GRID*NU)
FONT_HELP_TEXT_SIZE = 25
font_axis = pygame.font.SysFont('serif', FONT_AXIS_SIZE)
font_help_text = pygame.font.SysFont('serif', FONT_HELP_TEXT_SIZE)


SHOOT_TRACE_RADIUS = 5
HIT_CROSS_LINE_WIDTH = 5


WHITE = (255, 255, 255)
GREY = (169, 169, 169)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
