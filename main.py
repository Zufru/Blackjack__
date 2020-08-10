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
new_deck = Deck()
new_deck.shuffle()
shuffleddeck = new_deck.all_cards
new_dcard = ''
new_pcard = ''
ready = True
hit_dd = False

def ask_for_bet():
	"""
	ASKS IF PLAYER WANTS TO BET
	"""
	asking_for_bet = True
	while asking_for_bet:
		ask_for_pbet = input(f"\n{playername} Would you like to bet? \n(You have a balance of ${playerbalance}) ").lower()
		if ask_for_pbet == 'yes':
			asking_for_bet = False
			return ask_for_pbet
		elif ask_for_pbet == 'no':
			asking_for_bet = False
			pass
		else:
			print("Type either yes or no")

def deal_dealer_first_two():
	"""
	DEAL DEALERS FIRST TWO CARDS
	"""
	dealer_first_card = shuffleddeck.pop(0)
	dealer_second_card = shuffleddeck.pop(0)
	d_hand = [dealer_first_card, dealer_second_card]
	return d_hand

def check_dealer_total(dealer_cards):
	for i in dealer_cards:
		dealer_total = i.value + i.value
	return dealer_total

def deal_player_first_cards():
	"""
	DEAL PLAYERS FIRST TWO CARDS
	"""
	player_first_card = shuffleddeck.pop(0)
	player_second_card = shuffleddeck.pop(0)
	p_hand = [player_first_card, player_second_card]
	return p_hand

def compare_score(dealer_hand, player_hand):
	"""
	COMPARE SCORES AND DECIDE WINNER
	"""
	for i in dealer_hand:
		dealer_total = i.value + i.value
	for i in player_hand:
		player_total = i.value + i.value

	if player_total > 21:
		print("\n\nYou busted! " + str(dealer_total) + "\nPlayer total: " + str(player_total))
		bet = Player.player_bet
		player1.balance -= bet
	elif player_total == dealer_total:
		print("\n\nPUSH \nDealer: " + str(dealer_total) + "\nPlayer total: " + str(player_total))
	elif player_total > dealer_total:
		print("\n\nYou win! \nDealer: " + str(dealer_total) + "\nPlayer total: " + str(player_total))
		bet = Player.player_bet
		player1.balance += bet
	elif player_total < dealer_total:
		print("\n\nYou lose! \nDealer: " + str(dealer_total) + "\nPlayer total: " + str(player_total))
		bet = Player.player_bet
		player1.balance -= bet

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
		return True
		playing = False
	if hand_rank2 in faces and hand_rank1 == "Ace":
		print("||BLACKJACK|| YOU WIN! x2 bet")
		player1.balance += Player.player_bet * 2
		return True
		playing = False

while ready:
	start = input("\nAre you ready to begin? ").lower()
	if start == 'yes':
		ready = False
		playing = True
	elif start == 'no':
		quit()
	else:
		print("Please type yes or no")

while playing:
	player_hand = deal_player_first_cards()
	dealer_hand = deal_dealer_first_two()
	
	player_betting = ask_for_bet()
	if player_betting == "yes":
		player1.betchips()
	elif player_betting != "yes":
		pass

	print("\nYour cards are:")
	for i in player_hand:
		print(i)
		
	print("\n\n")
	check_blackjack(player_hand)
	if check_blackjack == True:
		playing = False
	
	print("\n\n\nThe dealers cards are:")
	for i in dealer_hand:
		print(i)
		
	#(HSDD) HIT/STAY/DOUBLEDOWN
	player_action_hsdd = input("\nWould you like to hit, stay, or double down? ").lower()
	if player_action_hsdd != 'stay':
		hit_dd = True
	while hit_dd:
		if player_action_hsdd == 'hit':
			player_hit = shuffleddeck.pop(0)
			player_hand.append(player_hit)
			print("\nYou hit, your cards are: ")
			for i in player_hand:
				print(i)
			hit_dd = False
		if player_action_hsdd == 'double down' and Player.player_bet != 0:
			Player.player_bet = Player.player_bet * 2
			player_hit = shuffleddeck.pop(0)
			player_hand.append(player_hit)
			hit_dd = False
	
	if player_action_hsdd == 'stay':
		print("\nYou stay with a hand of: ")
		for i in player_hand:
			print(i)
		playing = False

	for i in dealer_hand:
		total = i.value + i.value
		if total <=16:
			dealer_hit = shuffleddeck.pop(0)
			dealer_hand.append(dealer_hit)
	
	print("\nDealers hand: ")
	for i in dealer_hand:
		print(i)
	
	compare_score(dealer_hand, player_hand)
	playing = False
	
if check_blackjack == True:
	play_again = input("Would you like to play again? ").lower()
	if play_again == 'yes':
		playing = True
	else:
		quit()
	


