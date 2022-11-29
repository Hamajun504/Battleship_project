import ships
import enemy_field


class Player:
    def __init__(self, pos):
        self.ships = []
        self.field_shape = pos

    def place(self, pos1, pos2):
        x1 = (pos1 - self.field_shape[0]) * 10 // self.field_shape[2]
        y1 = (pos1 - self.field_shape[1]) * 10 // self.field_shape[3]
        x2 = (pos2 - self.field_shape[0]) * 10 // self.field_shape[2]
        y2 = (pos2 - self.field_shape[1]) * 10 // self.field_shape[3]
        if x1 == x2 or y1 == y2:
            length = abs(x1 - x2) + abs(y1 - y2)
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
        end = True
        for length in range(1, 5):
            num = 0
            for ship in self.ships:
                if ship.length == length:
                    num += 1
            end = end and (num + length) >= 5
        return end
