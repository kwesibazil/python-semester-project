class Cell(object):
    def __init__(self, x, y):
        # self.x = x
        # self.y = y
        self.pos = [x, y]
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0
        self.neighb = []