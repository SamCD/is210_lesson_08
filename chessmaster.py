#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time


class ChessPiece(object):
    """Creates a generic chess piece
    """

    prefix = ""
    def __init__(self, position):
        """Initializes the chess piece
        """
        
        self.position = position
        self.moves = []
        excep = '`{}` is not a legal start position'
        if self.is_legal_move(self.position) is False:
            raise ValueError(excep.format(position))


    def algebraic_to_numeric(self, tile):
        """Converts a square to integers
        """
        
        letters = ['a','b','c','d','e','f','g','h']
        pos = ()
        for i, j in tile.split():
            if i in letters and int(j) <= 8:
                pos = (letters.index(str(i)), int(j) - 1)
            else:
                pos = None
        return pos

    def is_legal_move(self, position):
        if self.algebraic_to_numeric(position) is None:
            legal = False
        else:
            legal = True
        return legal


    def move(self, position):
        """Moves a piece
        """
        
        if self.is_legal_move(position) is True:
            oldposition = self.position
            self.position = position
            move = (self.prefix + oldposition, self.prefix + self.position,\
                    time.time())
            self.moves.append(move)
            statement = self.moves
        else:
            move = False
        return move

class Rook(ChessPiece):
    """Creates a rook
    """

    prefix = "R"
        

    def is_legal_move(self, position):
        """Over rides ChessPiece.is_legal_move
        """
        if ChessPiece(position).is_legal_move(position) is True:
            for i, j in position.split():
                for a, b in self.position.split():
                    print a, b, i, j
                    if j != b and i != a:
                        legal = False
                    else:
                        legal = True
        else:
            legal = False
        return legal

class Bishop(ChessPiece):
    """ Creates a bishop
    """

    prefix = "B"

    def is_legal_move(self, position):
        """Over rides ChessPiece.is_legal_move
        """
        
        if ChessPiece(position).is_legal_move(position) is True:
            pos = ChessPiece(self.position).algebraic_to_numeric(self.position)
            newpos = ChessPiece(position).algebraic_to_numeric(position)
            legal = True if (abs(pos[0] - newpos[0]) \
                             == abs(pos[1] - newpos[1])) else False
            return legal

class King(ChessPiece):
    """ Creates the King
    """

    prefix = "K"

    def is_legal_move(self, position):
        """Over rides ChessPiece.is_legal_move
        """
        
        if ChessPiece(position).is_legal_move(position) is True:
            pos = ChessPiece(self.position).algebraic_to_numeric(self.position)
            newpos = ChessPiece(position).algebraic_to_numeric(position)
            legal = True if abs(pos[0] - newpos[0] <= 1) and\
                    abs(pos[1] - newpos[1]) <= 1 else False
            return legal
            
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
