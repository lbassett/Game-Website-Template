import BattleLineHands
import GlobalBattleLineVals


class BLstatus:

	def __init__(self):
		self.status = [[None,None,None,None,None,None,None]]*11 + [[None]]
		self.hands = self.initializehands()
		self.flags = [0,0,0,0,0,0,0,0,0]
		self.ones = 0
		self.twos = 0


	def initializehands(self):
		handlist = [hand(sortedlist,handvaldict)]*9
		return(handlist)
		
	def updatestatus(self):
		counter = 0
		for x in self.hands:
			newlist = []
			newlist += x.P1Hand
			newlist += [x.whowins()]
			newlist += x.P2Hand
			self.status[counter] = newlist
			counter+= 1
			self.status[11] = self.winner()

	def winner(self):
		if self.ones >=5:
			return(1)
		elif self.twos >= 5:
			return(2)
		else:
			one = 0
			two = 0
			for x in self.flags:
				if x == 1:
					one += 1
					two = 0
				elif x == 2:
					two += 1
					one = 0
				elif x == 0:
					two = 0
					one = 0
				pass
				if one == 3:
					return(1)
				elif two == 3:
					return(2)




