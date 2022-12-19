

class Ship:
    def __init__(self, pos_begin: tuple[int, int], pos_end: tuple[int, int]):
        self.cells = {}     #словарь с ключами - координатами клеток корабля, значениями - статусами клеток
        self.alive = True
        self.length = abs(pos_begin[0] - pos_end[0]) + abs(pos_begin[1] - pos_end[1]) + 1

        if pos_begin[0] == pos_end[0]:
            for i in range(abs(pos_begin[1]-pos_end[1]) + 1):
                self.cells[(pos_begin[0], min(pos_begin[1], pos_end[1]) + i)] = "alive"
        else:
            for i in range(abs(pos_begin[0] - pos_end[0]) + 1):
                self.cells[(min(pos_begin[0], pos_end[0]) + i, pos_begin[1])] = "alive"
