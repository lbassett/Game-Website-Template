import sys
from BLstatus import *
from TTTstatus import *

class game:
    
    def __init__(self, p1, idnum, name):
        self.idnum = idnum
        self.player1 = p1
        self.player2 = None
        self.winner = None
        self.move = 1 # 1 means it's player1's move, -1 means it's player2's move
        self.name = name
        self.status = self.initializestatus()

    def initializestatus(self):
    	if self.name == "Battle Lines":
    		newstatus = BLstatus()
    		return(newstatus)
        elif self.name == "Tic Tac Toe":
            newstatus = TTTstatus()
            return(newstatus)
    	else:
    		return(None)

    def getstatus(self):
    	return(self.status.statusinfo)

