class Spot:
    HOLE = 'hole'
    MONSTER = 'monster'
    GOLD = '**'

    def __init__(self,):
        self.contains = None
        self.stink = False
        self.breeze = False

    def set_clue(self, type):
        if type is self.HOLE:
            self.breeze = True
        elif type is self.MONSTER:
            self.stink = True

    def __repr__(self):
        if self.contains is None:
            value = ''
            if self.stink:
                value += 'S'
            if self.breeze:
                value += 'B'
            if value is '':
                value = None
            return str(value).ljust(10)

        return str(self.contains).ljust(10)
