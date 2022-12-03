import ships
import config


class Player:
    def __init__(self):
        self.ships = []
        self.field_shape = config.FIELD_RECT1
        self.enemy_field = []

    def place(self, pos1, pos2):
        x1 = (pos1[0] - self.field_shape[0]) * 10 // self.field_shape[2]
        y1 = (pos1[1] - self.field_shape[1]) * 10 // self.field_shape[3]
        x2 = (pos2[0] - self.field_shape[0]) * 10 // self.field_shape[2]
        y2 = (pos2[1] - self.field_shape[1]) * 10 // self.field_shape[3]
        if 0 <= x1 < 10 and 0 <= x2 < 10 and 0 <= y1 < 10 and 0 <= y2 < 10 and \
                self.ship_correct_placing_check(x1, x2, y1, y2):
            self.ships.append(ships.Ship((x1, y1), (x2, y2)))

    def ship_correct_placing_check(self, x1, x2, y1, y2):
        if x1 == x2 or y1 == y2:
            length = abs(x1 - x2) + abs(y1 - y2) + 1
            return self.check_size(length)
        else:
            return False

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

    def field_shape_update(self):
        pass
