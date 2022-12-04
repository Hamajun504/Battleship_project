import player
import config
import pygame




class View:
    def __init__(self, players: tuple[player.Player, player.Player], turn: int, screen: pygame.Surface):
        self.players = players
        self.turn = turn
        self.screen = screen
        self.my_field_screen = pygame.Surface((config.SIDE, config.SIDE))
        self.enemy_field_screen = pygame.Surface((config.SIDE, config.SIDE))
        self.grid = (config.SIDE - 12 * config.LINE_THICKNESS) // 10
        self.my_field_screen.fill(config.WHITE)
        self.enemy_field_screen.fill(config.WHITE)
    def draw_field(self):

        for i in range(12):
            pygame.draw.line(self.my_field_screen, config.GREY,
                             (0, self.grid * i),
                             (config.SIDE, self.grid * i), 2)
            pygame.draw.line(self.enemy_field_screen, config.GREY,
                             (self.grid * i, 0),
                             (self.grid * i, config.SIDE), 2)
            pygame.draw.line(self.enemy_field_screen, config.GREY,
                             (0, self.grid * i),
                             (config.SIDE, self.grid * i), 2)
            pygame.draw.line(self.my_field_screen, config.GREY,
                             (self.grid * i, 0),
                             (self.grid * i, config.SIDE), 2)

    def draw(self, mouse_holding):
        self.screen.fill(config.WHITE)
        self.draw_field()
        self.screen.blit(self.my_field_screen, (config.IDENT, config.IDENT))
        self.screen.blit(self.enemy_field_screen, (config.IDENT * 2 + config.SIDE, config.IDENT))
        self.draw_ships(mouse_holding)
        pygame.display.update()

    def next_turn(self):
        self.turn += 1

    def update_field_size(self):
        # TODO
        pass

    def draw_ships(self, mouse_holding):
        self.mouse_holding = mouse_holding

        if self.mouse_holding[0]:
            pass
        else:
            for ship in self.players[self.turn % 2].ships:
                for cell in ship.cells:
                    pygame.draw.rect(self.my_field_screen, config.DARK_GREEN,
                                     (cell[0], cell[1], self.grid, self.grid))
