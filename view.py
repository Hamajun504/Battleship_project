import player
import config
import pygame


class View:
    def __init__(self, players: tuple[player.Player, player.Player], turn: int, screen: pygame.Surface):
        self.players = players
        self.turn = turn
        self.screen = screen

        self.field_size = config.FIELD_SIZE
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

    def draw(self, status: dict):
        if status['neutral_screen']:
            self.write_change_turn()
        elif status['game_ended']:
            self.write_win(status)
        else:
            self.screen.fill(config.WHITE)
            self.screen.blit(self.grid, self.fields_pos[0])
            self.screen.blit(self.grid, self.fields_pos[1])
            self.draw_ships()
            self.draw_hit_cells()
            self.draw_enemy_ships()
            self.draw_numbers_and_letters()
            self.write_turn_tips(status)
            if status['turn_ended']:
                self.write_end_turn()
        pygame.display.update()

    def next_turn(self):
        self.turn += 1

    def draw_ships(self):
        for ship in self.players[self.turn % 2].ships:
            for cell in ship.cells.keys():
                pygame.draw.rect(self.screen, config.DARK_GREEN,
                                 (self.fields_pos[0][0] + cell[0] * self.field_size[0] // 10,
                                  self.fields_pos[0][1] + cell[1] * self.field_size[0] // 10,
                                  self.field_size[0] // 10, self.field_size[1] // 10))
                if ship.cells[cell] == "dead":
                    pygame.draw.line(self.screen, config.RED,
                                     (self.fields_pos[0][0] + cell[0] * self.field_size[0] // 10,
                                      self.fields_pos[0][1] + cell[1] * self.field_size[0] // 10),
                                     (self.fields_pos[0][0] + (cell[0] + 1) * self.field_size[0] // 10,
                                      self.fields_pos[0][1] + (cell[1] + 1) * self.field_size[1] // 10 + 1),
                                     config.HIT_CROSS_LINE_WIDTH)
                    pygame.draw.line(self.screen, config.RED,
                                     (self.fields_pos[0][0] + (cell[0] + 1) * self.field_size[0] // 10,
                                      self.fields_pos[0][1] + cell[1] * self.field_size[1] // 10),
                                     (self.fields_pos[0][0] + cell[0] * self.field_size[0] // 10,
                                      self.fields_pos[0][1] + (cell[1] + 1) * self.field_size[1] // 10),
                                     config.HIT_CROSS_LINE_WIDTH)

    def draw_enemy_ships(self):
        for ship in self.players[(self.turn + 1) % 2].ships:
            if ship.alive:
                for cell in ship.cells.keys():
                    if ship.cells[cell] == "dead":
                        pygame.draw.line(self.screen, config.RED,
                                         (self.fields_pos[1][0] + cell[0] * self.field_size[0] // 10,
                                          self.fields_pos[1][1] + cell[1] * self.field_size[1] // 10),
                                         (self.fields_pos[1][0] + (cell[0] + 1) * self.field_size[0] // 10,
                                          self.fields_pos[1][1] + (cell[1] + 1) * self.field_size[1] // 10 + 1),
                                         config.HIT_CROSS_LINE_WIDTH)
                        pygame.draw.line(self.screen, config.RED,
                                         (self.fields_pos[1][0] + (cell[0] + 1) * self.field_size[0] // 10,
                                          self.fields_pos[1][1] + cell[1] * self.field_size[1] // 10),
                                         (self.fields_pos[1][0] + cell[0] * self.field_size[0] // 10,
                                          self.fields_pos[1][1] + (cell[1] + 1) * self.field_size[1] // 10),
                                         config.HIT_CROSS_LINE_WIDTH)
            else:
                for cell in ship.cells.keys():
                    pygame.draw.rect(self.screen, config.RED,
                                     (self.fields_pos[1][0] + cell[0] * self.field_size[0] // 10,
                                      self.fields_pos[1][1] + cell[1] * self.field_size[1] // 10,
                                      self.field_size[0] // 10, self.field_size[1] // 10))

    def draw_hit_cells(self):
        for cell in self.players[self.turn % 2].shoten_cells:
            pygame.draw.circle(self.screen, config.BLACK,
                               (self.fields_pos[1][0] + cell[0] * self.field_size[0] // 10 + self.field_size[0] // 20,
                                self.fields_pos[1][1] + cell[1] * self.field_size[1] // 10 + self.field_size[1] // 20),
                               config.SHOOT_TRACE_RADIUS)
        for cell in self.players[(self.turn + 1) % 2].shoten_cells:
            pygame.draw.circle(self.screen, config.BLACK,
                               (self.fields_pos[0][0] + cell[0] * self.field_size[0] // 10 + self.field_size[0] // 20,
                                self.fields_pos[0][1] + cell[1] * self.field_size[1] // 10 + self.field_size[1] // 20),
                               config.SHOOT_TRACE_RADIUS)

    def draw_numbers_and_letters(self):
        letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}

        for x in letters.keys():
            letters_text = config.font_axis.render(letters[x], False, config.BLACK)
            for i in range(2):
                self.screen.blit(letters_text, (config.FIELDS_POS[i][0] + int(config.GRID * (x - 0.5)),
                                                config.FIELDS_POS[0][1] - config.FONT_AXIS_SIZE - 10))

        for x in range(10):
            numbers_text = config.font_axis.render(str(x + 1), False, config.BLACK)
            for i in range(2):
                self.screen.blit(numbers_text, (config.FIELDS_POS[i][0] - config.FONT_AXIS_SIZE,
                                                config.FIELDS_POS[0][1] + int(config.GRID * (x + 0.5)) - 10))

    def write_end_turn(self):
        """ ?????????? ???? ???????????? ?????? ?????????????????? ???????? """
        text_end_turn = '?????? ?????? ??????????????. ?????????????? Enter, ?????????? ???????????????? ?????? ???????????????????? ????????????.'
        text_pos = (100, config.SCREEN_HEIGHT - (config.SCREEN_HEIGHT - config.SIDE - config.IDENT) // 2)
        self.screen.blit(config.font_help_text.render(text_end_turn, False, config.BLACK), text_pos)

    def write_change_turn(self):
        """ ?????????? ???? ?????????????????????? ???????????? """
        if self.turn % 2 == 0:
            text_change_turn = '?????? ???????????? 2 ??????????????. ?????????????? Enter, ?????????? ???????????? ?????? ???????????? 1'
        else:
            text_change_turn = '?????? ???????????? 1 ??????????????. ?????????????? Enter, ?????????? ???????????? ?????? ???????????? 2'
        text_pos = (150, config.SCREEN_HEIGHT // 2)
        self.screen.fill(config.WHITE)
        self.screen.blit(config.font_help_text.render(text_change_turn, False, config.BLACK), text_pos)

    def write_win(self, status: dict):
        self.screen.fill(config.WHITE)
        text_win = '?????????? ' + str(status['winner']) + ' ??????????????'
        text_pos = (400, config.SCREEN_HEIGHT // 2)
        self.screen.blit(config.font_help_text.render(text_win, False, config.BLACK), text_pos)

    def write_turn_tips(self, status: dict):
        if self.turn <= 2:
            text = "???????????????????? ??????????????"
            text_pos = (config.SCREEN_WIDTH // 7, config.SCREEN_HEIGHT * 4 // 5)
            self.screen.blit(config.font_help_text.render(text, False, config.BLACK), text_pos)
            if not status["turn_ended"]:
                text2 = "?????????????? Space ?????? ??????????????????????????????"
                text2_pos = (config.SCREEN_WIDTH // 3,
                             config.SCREEN_HEIGHT - (config.SCREEN_HEIGHT - config.SIDE - config.IDENT) // 2)
                self.screen.blit(config.font_help_text.render(text2, False, config.BLACK), text2_pos)
        else:
            text = "??????????????????!"
            text_pos = (config.SCREEN_WIDTH * 2 // 3, config.SCREEN_HEIGHT * 4 // 5)
            self.screen.blit(config.font_help_text.render(text, False, config.BLACK), text_pos)

        if self.turn % 2 == 1:
            player_text = f"?????? ???????????? 1"
        else:
            player_text = f"?????? ???????????? 2"
        player_text_pos = (10, config.SCREEN_HEIGHT * 17 // 18)
        self.screen.blit(config.font_help_text.render(player_text, False, config.BLACK), player_text_pos)
