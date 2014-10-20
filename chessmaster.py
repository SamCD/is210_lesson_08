#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ChessPiece(object):
    import time

    def __init__(self, position):
        self.position = position
        self.prefix = ""
        self.moves = []
        excep = '`{}` is not a legal start position'
        if self.is_legal_move(self.position) is False:
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        letters = ['a','b','c','d','e','f','g','h']
        pos = ()
        for i, j in tile.split():
            if i in letters and int(j) < 8:
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
        import time
        if self.is_legal_move(position) is True:
            oldposition = self.position
            self.position = position
            move = (oldposition, self.position, time.time())
            self.moves.append(move)
            statement = self.moves
        else:statement = False
        return move
