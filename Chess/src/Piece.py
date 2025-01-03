class Piece:

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.hasMoved = False

    def move(self, x, y):

        ## check legality of move
        self.x = x
        self.y = y
        self.hasMoved = True

    def __str__(self):
        return self.color + " " + self.__class__.__name__ + " at " + str(self.x) + ", " + str(self.y)


class Pawn(Piece):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, x, y):
        super().move(x, y)

    def __str__(self):
        return super().__str__()