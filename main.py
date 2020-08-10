import random
from project_2 import Player
from project_2 import Deck

p_name = input("|||||||BLACKJACK||||||| \nWelcome to Black Jack, What is your name? ")
playername = p_name
playerbalance = 1000
player1 = Player(playername, playerbalance)
playing = False

def ask_for_bet():
	"""
	ASKS IF PLAYER WANTS TO BET
	"""
	return input(f"{playername} Would you like to bet? \n(You have a balance of ${playerbalance}) ").lower()

new_deck = Deck()
new_deck.shuffle()
shuffleddeck = new_deck.all_cards

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

start = input("\nAre you ready to begin? ").lower()

if start == 'yes':
	playing = True
elif start == 'no':
	quit()

while playing:
	player_hand = deal_player_first_cards()
	dealer_hand = deal_dealer_first_two()
	print(player_hand)
	print(dealer_hand)

	playing = False
	
#player_betting = ask_for_bet()
#if player_betting == "yes":
#	player1.betchips()
#elif player_betting != "yes":
#	pass

