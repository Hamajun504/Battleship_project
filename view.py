import player
import ships
import enemy_field
import game
import config
import pygame



class View:
    def __init__(self, players, turn, screen):
        self.players = players
        self.turn = turn
        self.side = config.SCREEN_WIDTH * config.MU
        self.indent = (config.SCREEN_HEIGHT - self.side*2)/3
        self.window_pos = ([self.indent, self.indent, self.side, self.side],
                           [self.side + self.indent * 2, self.indent, self.side, self.side])
        self.screen = screen
        self.color = config.WHITE
        self.my_field_screen = pygame.Surface((self.side, self.side))
        self.enemy_field_screen = pygame.Surface((self.side, self.side))


    def draw_fields(self):
        pygame.draw.rect(self.my_field, self.color, self.window_pos[0], 5)
        pygame.draw.rect(self.enemy_field, self.color, )

    def next_turn(self):
        self.turn += 1
