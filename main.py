import random
from project_2 import *

print("**********************************||||BLACKJACK||||******************************************")
information()
p_name = input("\nWelcome to Blackjack, What is your name? ")
playername = p_name
playerbalance = 1000
player1 = Player(playername, playerbalance)
playing = False
faces = ['Jack', 'Queen', 'King']

def ask_for_bet():
	"""
	ASKS IF PLAYER WANTS TO BET
	"""
	return input(f"{playername} Would you like to bet? \n(You have a balance of ${playerbalance}) ").lower()

new_deck = Deck()
new_deck.shuffle()
shuffleddeck = new_deck.all_cards
new_dcard = ''
new_pcard = ''

def deal_dealer_first_two():
	"""
	DEAL DEALERS FIRST TWO CARDS
	"""
	dealer_first_card = shuffleddeck.pop(0)
	dealer_second_card = shuffleddeck.pop(0)
	d_hand = [dealer_first_card, dealer_second_card]
	return d_hand

def deal_player_first_cards():
	"""
	DEAL PLAYERS FIRST TWO CARDS
	"""
	player_first_card = shuffleddeck.pop(0)
	player_second_card = shuffleddeck.pop(0)
	p_hand = [player_first_card, player_second_card]
	return p_hand
	
def check_blackjack(card):
	"""
	CHECKS IF PLAYER HAS BLACKJACK
	"""
	hand_rank1 = player_hand[0].rank
	hand_rank2 = player_hand[1].rank
	hand_value1 = values[hand_rank1]
	hand_value2 = values[hand_rank2]
	if hand_rank1 in faces and hand_rank2 == "Ace":
		print("||BLACKJACK|| YOU WIN! x2 bet")
		player1.balance += Player.player_bet * 2
	if hand_rank2 in faces and hand_rank1 == "Ace":
		print("||BLACKJACK|| YOU WIN!")
		player1.balance += Player.player_bet * 2

start = input("\nAre you ready to begin? ").lower()

if start == 'yes':
	playing = True
elif start == 'no':
	quit()

while playing:
	player_hand = deal_player_first_cards()
	dealer_hand = deal_dealer_first_two()
	print("\nYour cards are:")
	for i in player_hand:
		print(i)
	print("\n\n\nThe dealers cards are:")
	for i in dealer_hand:
		print(i)
	
	check_blackjack(player_hand)
	playing = False
	
#player_betting = ask_for_bet()
#if player_betting == "yes":
#	player1.betchips()
#elif player_betting != "yes":
#	pass
