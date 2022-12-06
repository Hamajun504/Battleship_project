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
        self.placing_stage = True
        self.clock = pygame.time.Clock()
        self.finished = False
        self.mouse_holding = (False, (0, 0))

    def run(self):
        while not self.finished:
            if self.placing_stage:
                self.view.draw()
                self.clock.tick(config.FPS)
                self.event_processing_in_placing_stage()
                if self.players[self.turn % 2].check_placing_end():
                    self.next_turn()
                    if self.turn == 3:
                        self.placing_stage = False

            else:
                self.view.draw()
                self.clock.tick(config.FPS)
                self.event_processing_out_of_placing_stage()

    def event_processing_in_placing_stage(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finished = True
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_holding = (True, (event.pos[0], event.pos[1]))
            elif event.type == pygame.MOUSEBUTTONUP:
                self.players[self.turn % 2].place(self.mouse_holding[1], event.pos)
                self.mouse_holding = (False, (0, 0))

    def event_processing_out_of_placing_stage(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finished = True
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                shot_done = self.players[self.turn % 2].shoot(event.pos)
                if shot_done:
                    self.damage_ship()
                    self.players[(self.turn + 1) % 2].declare_ships_killed()
                    self.players[self.turn % 2].mark_cells_near_destroyed_ship(self.players[(self.turn + 1) % 2].ships)
                    if self.check_game_go_on():
                        self.next_turn()
                    else:
                        print(f"Player {self.turn % 2 + 1} won")

    def damage_ship(self):
        for ship in self.players[(self.turn + 1) % 2].ships:
            for cell in ship.cells.keys():
                if self.players[self.turn % 2].shoten_cells[-1] == cell:
                    ship.cells[cell] = "dead"
                    break

    def next_turn(self):
        self.turn += 1
        self.view.next_turn()

    def check_game_go_on(self):
        for ship in self.players[(self.turn + 1) % 2].ships:
            if ship.alive:
                return True
        return False

