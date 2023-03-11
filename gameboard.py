# -*- coding: utf-8 -*-
from piece import Piece

class GameBoard:
    def _init_(self,piecesPerPlayer):
        self.state = self.createBoard(piecesPerPlayer)
        self.piecesA = self.getPieces(1)
        self.piecesB = self.getPieces(2)
        
    def _new_(cls, piecesPerPlayer):
        return super()._new_(cls)
    
    @classmethod
    def createBoard(self, piecesPerPlayer):
        #Assume-se que o piecesPerPlayer já foi verificado e é par e >= 4
        upperLine =     ['/','A','O','A','\\']
        midLineTop =    ['O','A','O','A','O']
        midLine =       ['O','O','O','O','O']
        midLineBottom = ['O','B','O','B','O']
        lowerLine =     ['\\','B','O','B','/']
        board = [upperLine,midLineTop,midLine,midLineBottom,lowerLine]
        piecesPerPlayer = piecesPerPlayer - 4
        while(piecesPerPlayer > 0):
            self.state = self.extendBoard(self)
            piecesPerPlayer -= 2
        return self.state
    
    @classmethod
    def extendBoard(self):
        circles = (len(self.state) // 2)
        firstLine = (circles * ['/']) + ['A','O','A'] + (circles * ['\\'])
        lastLine = (circles * ['\\']) + ['B','O','B'] + (circles * ['/'])
        for line in self.state:
            line.insert(0,line[0])
            line.append(line[len(line)-1])
        self.state.insert(0,firstLine)
        self.state.append(lastLine)
        return self.state
    
    @classmethod
    def getPieces(self,player):
        pieces = []
        if(player == 1):
            char = 'A'
        else:
            char = 'B'
        x = 1
        y = 1
        for line in self.state:
            for spot in line:
                if (self.state[x-1][y-1] == char):
                   pieces = pieces + Piece(x,y)
                x += 1
            y = 1
        return pieces
    
    @classmethod
    def displayBoard(self):
        side = len(self.state)
        header = [str(x) for x in range(side + 1)]
        header.remove("0")
        h_str = "    " + ' '.join(header)
        print(h_str)
        i = 1
        for line in self.state:
            space = (4 - len(str(i))) * " "
            l = str(i) + space + ' '.join(line)
            print(l)
            i += 1
        return
    
    @classmethod
    def isPlayerPiece(self,piece,player):
        if (player == 1):
            return (piece in self.piecesA)
        elif (player == 2):
            return (piece in self.piecesB)
        
        