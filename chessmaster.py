#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ChessPiece(object):
    """Creates a generic chess piece
    """
    
    import time


    def __init__(self, position):
        """Initializes the chess piece
        """
        
        self.position = position
        self.prefix = ""
        self.moves = []
        self.is_legal_move = self.algebraic_to_numeric(position)
        excep = '`{}` is not a legal start position'
        if self.is_legal_move is False:
            raise ValueError(excep.format(position))


    def algebraic_to_numeric(self, tile):
        """Converts a square to integers
        """
        
        letters = ['a','b','c','d','e','f','g','h']
        pos = ()
        for i, j in tile.split():
            if i in letters and int(j) < 8:
                pos = (letters.index(str(i)), int(j) - 1)
            else:
                pos = None
        return pos


    def move(self, position):
        """Moves a piece
        """
        
        import time
        if self.is_legal_move is True:
            oldposition = self.position
            self.position = position
            move = (oldposition, self.position, time.time())
            self.moves.append(move)
            statement = self.moves
        else:statement = False
        return move

class Rook(ChessPiece):
    """Creates a rook
    """


    def __init__(self, position):
        """Initializes the rook
        """
        
        self.prefix = "R"

    def is_legal_move(self, position):
        self.newpos = position
        if self.is_legal_move is True:
            if self.newpos.split()[1] != self.position.split()[1] or\
               self.newpos.split()[0] != self.position.split()[0]:
                self.is_legal_move is False
            
class ChessMatch(object):
    """Creates a game of chess
    """


    def __init__(pieces=None):
        """Initializes the Chess Match
        """
        
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            log = []


    def reset(self):
        """Resets the board
        """
        
        pieces = {'Ra1': Rook('a1'), 'Rh1': Rook('h1'), 'Ra8': Rook('a8'),
                  'Rh8': Rook('h8'), 'Bc1': Bishop('c1'), 'Bf1': Bishop('f1'),
                  'Bc8': Bishop('c8'), 'Bf8': Bishop('f8'), 'Ke1': King('e1'),
                  'Ke8': King('e8')}


    def move(self, piece, destination):
        """Moves the pieces
        """
        import time
        if is_legal_move(destination) is True:
            move = (self.position, destination, time.time())
            log.append(move)
            pieces[piece] = pieces.pop[destination]
