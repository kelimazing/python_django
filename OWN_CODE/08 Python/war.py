#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class (List contianing cards). This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("New Deck Created!")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling Cards")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    '''
    This is the Hand class (List containing cards). Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        print("Cards distributed to players")
        self.cards = cards

    def __str__(self):
        return f"Contains {len(self.cards)} cards"

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop(0)


class Player:
    """
    This is the Player class (Player name and Hand), which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has placed : {drawn_card}")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            for x in range(len(self.hand.cards)):
                war_cards.append(self.hand.remove_card())

        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())

        return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) > 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create deck
deck = Deck()
deck.shuffle()
d1,d2 = deck.split_in_half()

# Assign Players and hand
comp = Player("Computer", Hand(d1))

user = input("What's your name? ")
player = Player(user, Hand(d2))

# Start GAME
# initiate round and war counts
rounds = 1
war_count = 0
pot = [] # Set up pot

# While players still have cards, proceed
while player.still_has_cards() and comp.still_has_cards():
    print(f"Round {rounds}")

    # Each player draws a card from their respective hands
    card1 = comp.play_card()
    card2 = player.play_card()
    pot.extend([card1, card2]) # Add cards to pot

    # If war (both cards are equal in value)
    if card1[1] == card2[1]:
        war_count += 1
        print("War!")

        # Each player adds 3 cards from their hand to the pot
        war1 = comp.remove_war_cards()
        war2 = player.remove_war_cards()
        pot.extend(war1 + war2)
        continue # Repeat to draw single cards until one card is higher

    # If player card is higher in value
    elif RANKS.index(card1[1]) > RANKS.index(card2[1]):
        player.hand.add(pot)

    # If computer card is higher in value
    else:
        comp.hand.add(pot)

    rounds += 1 # Increment round for next round
    pot = [] # Clear pot for next round

    # Round Limit to avoid infinite loop
    if rounds == 1000:
        break

# If player has more cards than computer
if len(player.hand.cards) > len(comp.hand.cards):
    player.hand.add(pot) # Add pot to hand in case of win via Round Limit
    print(f"{player.name} wins!")

# If computer has more cards than player
else:
    comp.hand.add(pot) # Add pot to hand in case of win via Round Limit
    print(f"{comp.name} wins!")

# Game Stats
print(f"{player.name}'s cards : {len(player.hand.cards)}")
print(f"{comp.name}'s cards : {len(comp.hand.cards)}")
# print(f"Total cards : {len(comp.hand.cards) + len(player.hand.cards)}")
print(f"Total Rounds : {rounds - 1}")
print(f"Total Wars : {war_count}")
