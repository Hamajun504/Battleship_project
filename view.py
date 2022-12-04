import player
import config
import pygame


class View:
    def __init__(self, players: tuple[player.Player, player.Player], turn: int, screen: pygame.Surface):
        self.players = players
        self.turn = turn
        self.screen = screen

        self.field_size = config.FIELD_SiZE
        self.fields_pos = config.FIELDS_POS

        self.grid = pygame.Surface((self.field_size[0] + 1, self.field_size[1] + 1))
        self.grid.fill(config.WHITE)
        for i in range(11):
            pygame.draw.line(self.grid, config.GREY,
                             (0, self.field_size[1] * i // 10),
                             (self.field_size[0], self.field_size[1] * i // 10), 2)
            pygame.draw.line(self.grid, config.GREY,
                             (self.field_size[0] * i // 10, 0),
                             (self.field_size[0] * i // 10, self.field_size[1]), 2)

    def draw(self):
        self.screen.fill(config.WHITE)
        self.screen.blit(self.grid, self.fields_pos[0])
        self.screen.blit(self.grid, self.fields_pos[1])
        self.draw_ships()
        pygame.display.update()

    def next_turn(self):
        self.turn += 1

    def update_field_size(self):
        # TODO
        pass

    def draw_ships(self):
        for ship in self.players[self.turn % 2].ships:
            for cell in ship.cells:
                pygame.draw.rect(self.screen, config.DARK_GREEN,
                                 (config.FIELD_RECT1[0] + cell[0] * config.FIELD_RECT1[2] // 10,
                                  config.FIELD_RECT1[1] + cell[1] * config.FIELD_RECT1[3] // 10,
                                  config.FIELD_RECT1[2] // 10, config.FIELD_RECT1[3] // 10))
