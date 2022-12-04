import ships
import config


class Player:
    def __init__(self):
        self.ships = []
        self.enemy_field = []

    def place(self, pos1, pos2):
        x1 = (pos1[0] - config.IDENT) * 10 // config.SIDE
        y1 = (pos1[1] - config.IDENT) * 10 // config.SIDE
        x2 = (pos2[0] - config.IDENT) * 10 // config.SIDE
        y2 = (pos2[1] - config.IDENT) * 10 // config.SIDE
        if x1 == x2 or y1 == y2:
            length = abs(x1 - x2) + abs(y1 - y2) + 1
            if self.check_size(length):
                self.ships.append(ships.Ship((x1, y1), (x2, y2)))

    def check_size(self, length):
        """ проверяет, что можно поставить ещё корабли длины length """
        num = 0
        for ship in self.ships:
            if ship.length == length:
                num += 1
        return num + length < 5

    def check_placing_end(self):
        """ возвращает True, если расстановка закончена """
        end = True
        for length in range(1, 5):
            num = 0
            for ship in self.ships:
                if ship.length == length:
                    num += 1
            end = end and (num + length) >= 5
        return end
