import ships
import player
import view
import pygame
import config


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.players = (player.Player(), player.Player())
        self.view = view.View()
        self.placing_stage = True
        self.turn = 1
        self.clock = pygame.time.Clock()
        self.finished = False
        self.mouse_holding = (False, (0, 0))


    def draw(self):
        pass

    def run(self):
        while not self.finished:
            if self.placing_stage:
                self.view.draw()
                self.clock.tick(config.FPS)
                self.event_processing()

    def event_processing(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.finished = True
            elif event == pygame.MOUSEBUTTONDOWN:
                self.mouse_holding = (True, (event.pos[0], event.pos[0]))
            elif event == pygame.MOUSEBUTTONUP:
                player[self.turn % 2].place(self.mouse_holding[1], event.pos)
                self.mouse_holding = (False, (0, 0))
