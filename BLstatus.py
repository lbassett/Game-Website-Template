from BattleLineHands import *
from GlobalBattleLineVals import *
import random


class BLstatus:

	def __init__(self):
		self.hands = self.initializehands()
		self.flags = [0,0,0,0,0,0,0,0,0]
		self.ones = 0
		self.twos = 0
		self.deck = self.initializedeck()
		self.playercards = self.initializecards()
		self.statusinfo = [[None,None,None,None,None,None,None]]*9 + self.playercards + [[None]]



	def initializehands(self):
		handlist = [hand(sortedhands,handvaldict)]*9
		return(handlist)

	def initializedeck(self):
		deck = []
		for x in range(60):
			deck += [x]
		random.shuffle(deck)
		return(deck)

	def initializecards(self):
		cards = [self.deck[0:7],self.deck[7:14]]
		self.deck = self.deck[14:]
		return(cards)


	def makemove(self, player, cardnum, handnum):
		card = self.playercards[player][cardnum]
		del(self.playercards[player][cardnum])
		if player == 0:
			self.hands[handnum].P1Hand += [card]
		self.playercards[player] += [newcard]
		else:
			self.hands[handnum].P2Hand += [card]
		newcard = self.deck[0]
		self.playercards[player] += [newcard]
		self.deck = self.deck[1:]
		self.updatestatus()

	def updatestatus(self):
		counter = 0
		for x in self.hands:
			newlist = []
			newlist += x.P1Hand
			victor = x.whowins
			if victor == 1:
				self.ones += 1
			elif victor == 2:
				self.twos += 2
			newlist += [victor]
			newlist += x.P2Hand
			self.statusinfo[counter] = newlist
			counter+= 1
			self.status[11] = self.winner()


	def winner(self):
		onewins = False
		twowins = False
		if self.ones >=5:
			onewins = True
		elif self.twos >= 5:
			twowins = True
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
					onewins = True
				elif two == 3:
					twowins = True
		if onewins and twowins:
			return(3) # 3 in the case of a tie
		elif onewins:
			return(1)
		elif twowins:
			return(2)
		else:
			return(0)



z = BLstatus()
print(z.flags)
