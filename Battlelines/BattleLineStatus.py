import BattleLineHands
import GlobalBattleLineVals


class BLstatus:

	def __init__(self):
		self.status = [[None,None,None,None,None,None,None]]*9
		self.hands = self.initializehands()
		self.flags = [0,0,0,0,0,0,0,0,0]


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
			self.hands[counter] = newlist
			counter+= 1
