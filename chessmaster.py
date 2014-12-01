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
        
        if not ChessPiece.is_legal_move(self, position):
            excep = "'{}' is not a legal start position"
            raise ValueError(excep.format(position))
        self.position = position
        self.moves = []
        excep = '`{}` is not a legal start position'
        if self.is_legal_move(self.position) is False:
            raise ValueError(excep.format(position))


    def algebraic_to_numeric(self, tile):
        """Converts a square to integers
        """
        
        xcoord = 'abcdefgh'.find(tile[0])
        ycoord = int(tile[1]) - 1
        retval = None
        if xcoord > -1 and 0 <= ycoord <= 7:
            retval = (xcoord, ycoord)
     
        return retval


    def is_legal_move(self, position):
        """Is move legal?"""
        return True if self.algebraic_to_numeric(position) else False
        

    def move(self, position):
        """Moving"""
        retval = False
        if self.is_legal_move(position):
            oldpos = self.position
            self.position = position
            retval = (oldpos, position, time.time())
            self.moves.append(retval)

        return retval

class Rook(ChessPiece):
    """Creates the rook"""
    prefix = 'R'

    def is_legal_move(self, position):
        """Moving the rook"""
        newpos = self.algebraic_to_numeric(position)
        oldpos = self.algebraic_to_numeric(self.position)
        
        retval = False
        if newpos and (newpos[0] == oldpos[0] or newpos[1] == oldpos[1]):
            retval = True
        return retval


class Bishop(ChessPiece):
    """Creates the bishop"""

    prefix = 'B'

    def is_legal_move(self, position):
        """Legal?"""
        newpos = self.algebraic_to_numeric(position)
        oldpos = self.algebraic_to_numeric(self.position)

        diagonal =  abs(oldpos[0] - newpos[0]) == abs(oldpos[1] - newpos[1])
        return True if diagonal and newpos != oldpos else False


class King(ChessPiece):
    """Creates the king"""

    prefix = 'K'


    def is_legal_move(self, position):
        """Legal?"""
        newpos = self.algebraic_to_numeric(position)
        oldpos = self.algebraic_to_numeric(self.position)

        diagonal = abs(oldpos[0] - newpos[0]) == abs(oldpos[1] - newpos[1])
        sides = newpos[0] == oldpos[0] or newpos[1] == oldpos[1]
        return True if diagonal and sides and newpos != oldpos else False


class ChessMatch(object):
    """Chess Match"""


    def __init__(self, pieces=None):
        """Sets the board"""
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
        self.log = []


    def reset(self):
        """Resets the match"""
        self.log = []
        self.pieces = {
            'Ra1': Rook('a1'),
            'Rh1': Rook('h1'),
            'Ra8': Rook('a8'),
            'Rh8': Rook('h8'),
            'Bc1': Bishop('c1'),
            'Bf1': Bishop('f1'),
            'Bc8': Bishop('c8'),
            'Bf8': Bishop('f8'),
            'Kc1': King('c1'),
            'Kc8': King('c8'),
        }


    def move(self, piece, position):
        """Moves the pieces"""
        pinstance = self.pieces[piece]
        retval = pinstance.move(position)

        if retval:
            self.log.append(retval)
            self.pieces[pinstance.prefix + position] - self.pieces.pop(piece)

        return retval

    def __len__(self):
        """Length"""
        return len(self,log)
