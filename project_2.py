import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
			'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
			
values = {'Two':2, 'Three': 3, 'Four':4, 'Five':5, 'Six':6, 'Seven': 7, 'Eight': 8,
			'Nine': 9, 'Ten':10, 'Jack': 11, 'Queen':11, 'King':11, 'Ace':11}

			
class Card:
	"""
	CARD CLASS, DESCRIBES CARDS AND SETS THEM
	"""
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]
		
	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:
	"""
	DECK CLASS SHUFFLY, STAY, DEAL CARDS
	"""
	def __init__(self):
		self.all_cards = []
		self.new_cards = []

		for suit in suits:
			for rank in ranks:
				created_cards = Card(suit, rank)
				self.all_cards.append(created_cards)
		
	def shuffle(self):
		return random.shuffle(self.all_cards)
	
	def stay(self):
		pass
	
	def deal_one(self):
		return self.all_cards.pop()
		
	def __str__(self):
		return self.rank + " of " + self.suit

class Player:
	"""
	PLAYER CLASS DEFINING BET AND SAVING IT TO PLAYER_BET IF PLAYER WINS
	"""
	player_bet = int(0)
	
	def __init__(self, player, balance):
		self.player = player
		self.balance = balance
		
	def betchips(self):
		how_much_bet = int(input("How much would you like to bet? "))
		if self.balance > how_much_bet:
			player_bet = how_much_bet
			self.balance -= player_bet
			print(f"You have bet ${player_bet} on this hand!")
		elif self.balance < how_much_bet:
			print(f"You only have ${self.balance} you can not bet more than that!")
			
			
			
	def __str__(self):
		return self.player + ' has a balance of ' + str(self.balance) 


def information():
	"""
	JUST AN INFORMATION SECTION
	"""
	info2 = print("************************************|HOW TO PLAY|********************************************")
	info3 = print("****                   All cards are equivalent to their stated value.                   ****")
	info4 = print("****                   Face cards hold a value of 11.                                    ****")
	info5 = print("****                   A face card with a ACE on your first two cards is a blackjack.    ****")
	info6 = print("****                   Blackjack doubles your bet.                                       ****")
	info7 = print("*********************************************************************************************")
