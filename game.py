import player
import view
import pygame
import config


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.players = (player.Player(), player.Player())
        self.turn = 1
        self.view = view.View(self.players, self.turn, self.screen)
        self.clock = pygame.time.Clock()
        self.mouse_holding = (False, (0, 0))
        self.status = {'placing_stage': True, 'finished': False, 'turn_ended': False, 'neutral_screen': False,
                       'hit': False, 'game_ended': False, 'winner': 0}

    def run(self):
        """ Основной цикл """
        while not self.status['finished']:
            if self.status['placing_stage']:
                self.view.draw(self.status)
                if self.status['turn_ended']:
                    self.clock.tick(config.FPS)
                self.event_processing_in_placing_stage()
                if self.players[self.turn % 2].check_placing_end() and not self.status['neutral_screen']:
                    self.end_turn()
                    if self.turn == 2:
                        self.status['placing_stage'] = False

            else:
                self.view.draw(self.status)
                self.clock.tick(config.FPS)
                self.event_processing_out_of_placing_stage()

    def event_processing_in_placing_stage(self):
        """ Обработка событий в стадии расстановки кораблей """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status['finished'] = True
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_holding = (True, (event.pos[0], event.pos[1]))
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.players[self.turn % 2].place(self.mouse_holding[1], event.pos)
                self.mouse_holding = (False, (0, 0))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.status['turn_ended']:
                        self.status['neutral_screen'] = True
                        self.status['turn_ended'] = False
                    elif self.status['neutral_screen']:
                        self.start_turn()
                elif event.key == pygame.K_SPACE:
                    self.players[self.turn % 2].ships = []
                    self.players[self.turn % 2].auto_placing()

    def event_processing_out_of_placing_stage(self):
        """ Обработка событий вне стадии расстановки кораблей"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status['finished'] = True
                break
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not self.status['turn_ended']:
                shot_done = self.players[self.turn % 2].shoot(event.pos)
                if shot_done:
                    self.damage_ship()
                    self.players[(self.turn + 1) % 2].declare_ships_killed()
                    self.players[self.turn % 2].mark_cells_near_destroyed_ship(self.players[(self.turn + 1) % 2].ships)
                    if self.check_game_go_on():
                        if not self.status['hit']:
                            self.end_turn()
                    else:
                        self.status['game_ended'] = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.status['turn_ended']:
                        self.status['neutral_screen'] = True
                        self.status['turn_ended'] = False
                    elif self.status['neutral_screen']:
                        self.start_turn()
                    break

    def damage_ship(self):
        """ Проверка попаданий при выстреле, меняет статус 'hit' """
        self.status['hit'] = False
        for ship in self.players[(self.turn + 1) % 2].ships:
            for cell in ship.cells.keys():
                if self.players[self.turn % 2].shoten_cells[-1] == cell:
                    ship.cells[cell] = "dead"
                    self.status['hit'] = True
                    break



    def end_turn(self):
        self.status['turn_ended'] = True

    def start_turn(self):
        self.turn += 1
        self.view.next_turn()
        self.status['neutral_screen'] = False
        self.status['turn_ended'] = False

    def check_game_go_on(self):
        """ Проверка неокончания игры по причине победы """
        for ship in self.players[(self.turn + 1) % 2].ships:
            if ship.alive:
                return True
        self.status['winner'] = self.turn % 2
        return False



