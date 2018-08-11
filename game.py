
class game:
    
    def __init__(self, p1, idnum, name):
        self.idnum = idnum
        self.player1 = p1
        self.player2 = None
        self.winner = None
        self.move = 1 # 1 means it's player1's move, -1 means it's player2's move
        self.name = name
        self.status = None

