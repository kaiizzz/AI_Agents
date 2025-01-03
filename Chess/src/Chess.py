from Piece import *

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.whitePieces = []
        self.blackPieces = []
        self.moveHistory = []