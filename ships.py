

class Ship:
    def __init__(self, pos_begin, pos_end):
        self.cells = []
        self.alive = True
        self.length = abs(pos_begin[0] - pos_end[0]) + abs(pos_begin[1] - pos_end[1]) + 1

        if pos_begin[0] == pos_end[0]:
            for i in range(abs(pos_begin[1]-pos_end[1]) + 1):
                self.cells.append((pos_begin[0], min(pos_begin[1], pos_end[1]) + i))
        else:
            for i in range(abs(pos_begin[0] - pos_end[0]) + 1):
                self.cells.append((min(pos_begin[0], pos_end[0]) + i, pos_begin[1]))

