from copy import deepcopy

class hand:
    def __init__(self, slist, hv):
        self.P1Hand = []
        self.P2Hand = []
        self.list0 = slist
        self.P1V = deepcopy(hv)
        self.P2V = deepcopy(hv)
        self.winner = None

    def getbestvalue(x):
        w=0
        if x ==1:
            while self.P1V[self.list0[w]] == 0:
                w +=1
            return(self.P1V[self.list0[w]])
        else:
            while self.P2V[self.list0[w]] == 0:
                w +=1
            return(self.P2V[self.list0[w]])            

    def whowins():
        a = len(self.P1Hand)
        b = len(self.P2Hand)
        if a!= 3 and b!= 3:
            return(0)
        else:
            x = self.getbestvalue(1)
            y = self.getbestvalue(2)
            if a != 3:
                if x <= y:
                    return(2)
                else:
                    return(0)
            elif b != 3:
                if x >= y:
                    return(1)
                else:
                    return(0)
            else:
                if x>y:
                    return(1)
                else:
                    return(2)

    def hascard(z,p):
        if p == 1:            
            for x in range(34220):
                if (z in self.list0[x]) == False:
                    self.P1V[self.list0[x]] = 0
        if p == 2:
            for x in range(34220):
                if (z in self.list0[x]) == False:
                    self.P2V[self.list0[x]] = 0
        
    def hasntcard(z,p):
        if p == 1:            
            for x in range(34220):
                if z in self.list0[x]:
                    self.P1V[self.list0[x]] = 0
        if p == 2:
            for x in range(34220):
                if z in self.list0[x]:
                    self.P2V[self.list0[x]] = 0

    
        
        

    




