import player
import ships
import game
import config
import pygame



class View:
    def __init__(self, players, turn, screen):
        self.players = players
        self.turn = turn
        self.screen = screen

        self.grid = pygame.Surface((config.FIELD_RECT1[2] + 1, config.FIELD_RECT1[3] + 1))
        self.grid.fill(config.WHITE)
        for i in range(11):
            pygame.draw.line(self.grid, config.GREY,
                             (0, config.FIELD_RECT1[3] * i // 10), (config.FIELD_RECT1[2], config.FIELD_RECT1[3] * i // 10),
                             2)
            pygame.draw.line(self.grid, config.GREY,
                             (config.FIELD_RECT1[2] * i // 10, 0), (config.FIELD_RECT1[2] * i // 10, config.FIELD_RECT1[3]),
                             2)

    def draw(self):
        self.screen.fill(config.WHITE)
        self.screen.blit(self.grid, (config.FIELD_RECT1[0], config.FIELD_RECT1[1]))
        self.screen.blit(self.grid, (config.FIELD_RECT2[0], config.FIELD_RECT2[1]))
        pygame.display.update()

    def next_turn(self):
        self.turn += 1

    def update_field_size(self):
        # TODO
        pass

